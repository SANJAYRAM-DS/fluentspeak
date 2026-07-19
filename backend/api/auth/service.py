"""
Authentication Service.

This module contains the core business logic. It takes validated input from
the schemas, applies business rules (validators), queries/modifies the
database via the repository, and returns the response payload.
"""
from django.db import transaction
from django.http import HttpRequest

from backend.api.auth import repository, validators
from backend.api.auth.schemas import (
    RegisterRequest,
    LoginRequest,
    RefreshTokenRequest,
    ChangePasswordRequest,
    ForgotPasswordRequest,
    ResetPasswordRequest,
    UpdateProfileRequest,
    AuthResponse,
    TokenResponse,
    CurrentUserResponse,
    MessageResponse
)
from backend.core.security import verify_password, generate_reset_token, hash_password
from backend.core.jwt import create_token_pair, decode_token
from backend.core.utils import get_client_ip, get_user_agent
from backend.core.exceptions import AuthenticationError, NotFoundError, ValidationError, ConflictError


def register(data: RegisterRequest, request: HttpRequest) -> AuthResponse:
    """
    Registers a new user, creates their profile, logs the event, 
    and generates initial tokens. All wrapped in a transaction so
    if any step fails, nothing is saved to the database.
    """
    try:
        validators.validate_registration(data)
    except (ValidationError, ConflictError) as e:
        repository.create_audit_log(
            user=None,
            action="REGISTER_FAILED",
            ip_address=get_client_ip(request),
            user_agent=get_user_agent(request),
            metadata={"email": data.email, "reason": str(e)}
        )
        raise e

    with transaction.atomic():
        # 1. Create User
        user = repository.create_user(
            email=data.email,
            password=data.password
        )
        
        # 2. Create Profile
        profile = repository.create_user_profile(
            user=user,
            first_name=data.first_name,
            last_name=data.last_name
        )
        
        # 3. Audit Log
        repository.create_audit_log(
            user=user,
            action="REGISTER",
            ip_address=get_client_ip(request),
            user_agent=get_user_agent(request)
        )
        
        # 4. Generate Tokens
        tokens = create_token_pair(user)
        
    return AuthResponse(
        tokens=TokenResponse(**tokens),
        user=user,
        profile=profile
    )


def login(data: LoginRequest, request: HttpRequest) -> AuthResponse:
    """
    Verifies credentials, updates last_login, logs the event,
    and returns auth tokens.
    """
    user = repository.get_user_by_email(data.email)
    
    # Generic failure message to prevent email enumeration
    if not user or not verify_password(data.password, user.password):
        repository.create_audit_log(
            user=user,
            action="LOGIN_FAILED",
            ip_address=get_client_ip(request),
            user_agent=get_user_agent(request),
            metadata={"email": data.email, "reason": "Invalid credentials"}
        )
        raise AuthenticationError("Invalid email or password.")
        
    if not user.is_active:
        repository.create_audit_log(
            user=user,
            action="LOGIN_FAILED",
            ip_address=get_client_ip(request),
            user_agent=get_user_agent(request),
            metadata={"email": data.email, "reason": "Account deactivated"}
        )
        raise AuthenticationError("This account has been deactivated.")
        
    # Update last login timestamp
    repository.update_last_login(user)
    
    # Create success audit log
    repository.create_audit_log(
        user=user,
        action="LOGIN_SUCCESS",
        ip_address=get_client_ip(request),
        user_agent=get_user_agent(request)
    )
    
    tokens = create_token_pair(user)
    
    return AuthResponse(
        tokens=TokenResponse(**tokens),
        user=user,
        profile=user.profile
    )


def refresh_token(data: RefreshTokenRequest, request: HttpRequest) -> TokenResponse:
    """
    Takes a valid refresh token and returns a fresh pair of access/refresh tokens.
    """
    try:
        # decode_token will raise AuthenticationError if expired or invalid
        payload = decode_token(data.refresh, token_type="refresh")
        
        user_id = payload.get("sub")
        user = repository.get_user_by_id(user_id)
        
        if not user or not user.is_active:
            raise AuthenticationError("User not found or inactive.")
            
        repository.create_audit_log(
            user=user,
            action="TOKEN_REFRESH",
            ip_address=get_client_ip(request),
            user_agent=get_user_agent(request)
        )
            
        tokens = create_token_pair(user)
        return TokenResponse(**tokens)
    except AuthenticationError as e:
        repository.create_audit_log(
            user=None,
            action="TOKEN_REFRESH_FAILED",
            ip_address=get_client_ip(request),
            user_agent=get_user_agent(request),
            metadata={"reason": str(e)}
        )
        raise e


def logout(user, request: HttpRequest) -> MessageResponse:
    """
    Stateless JWT logout simply logs the action. The client is responsible
    for deleting the token on their end. (In a stateful setup, we'd blacklist the token).
    """
    repository.create_audit_log(
        user=user,
        action="LOGOUT",
        ip_address=get_client_ip(request),
        user_agent=get_user_agent(request)
    )
    return MessageResponse(message="Successfully logged out.")


def get_current_user(user) -> CurrentUserResponse:
    """Returns the currently authenticated user and their profile."""
    return CurrentUserResponse(
        user=user,
        profile=user.profile
    )


def update_profile(user, data: UpdateProfileRequest) -> CurrentUserResponse:
    """Updates the user's profile with provided fields."""
    update_data = data.model_dump(exclude_unset=True)
    
    with transaction.atomic():
        profile = repository.update_user_profile(user, update_data)
    
    return CurrentUserResponse(
        user=user,
        profile=profile
    )


def change_password(user, data: ChangePasswordRequest, request: HttpRequest) -> MessageResponse:
    """Updates a user's password if they know their old one."""
    try:
        validators.validate_password_match(data.new_password, data.new_password_confirm)
        
        if not verify_password(data.old_password, user.password):
            raise ValidationError("Incorrect old password.")
            
        validators.validate_password_strength(data.new_password)
    except ValidationError as e:
        repository.create_audit_log(
            user=user,
            action="PASSWORD_CHANGE_FAILED",
            ip_address=get_client_ip(request),
            user_agent=get_user_agent(request),
            metadata={"reason": str(e)}
        )
        raise e
    
    with transaction.atomic():
        repository.update_password(user, data.new_password)
        
        repository.create_audit_log(
            user=user,
            action="PASSWORD_CHANGED",
            ip_address=get_client_ip(request),
            user_agent=get_user_agent(request)
        )
        
    return MessageResponse(message="Password changed successfully.")


def forgot_password(data: ForgotPasswordRequest, request: HttpRequest) -> MessageResponse:
    """
    Initiates the password reset flow. Generates a secure token.
    For V1, it returns the token in the response (simulate email sending).
    """
    user = repository.get_user_by_email(data.email)
    
    # We still return success even if user doesn't exist to prevent enumeration.
    # We execute a dummy hash to prevent timing attacks.
    if not user:
        hash_password("dummy_password_to_simulate_work")
        return MessageResponse(message="If an account with that email exists, a reset link has been sent.")
        
    token = generate_reset_token()
    repository.save_reset_token(user, token)
    
    # In V2, we would send an email here instead of returning the token.
    return MessageResponse(message=f"Reset token (for testing): {token}")


def reset_password(data: ResetPasswordRequest, request: HttpRequest) -> MessageResponse:
    """Verifies the reset token and updates the password."""
    try:
        validators.validate_password_match(data.new_password, data.new_password_confirm)
        validators.validate_password_strength(data.new_password)
        
        user = repository.get_user_by_reset_token(data.token)
        
        if not user:
            raise ValidationError("Invalid or expired reset token.")
    except ValidationError as e:
        # We don't have the user object if the token is invalid, but we can log the IP
        repository.create_audit_log(
            user=None,
            action="PASSWORD_RESET_FAILED",
            ip_address=get_client_ip(request),
            user_agent=get_user_agent(request),
            metadata={"reason": str(e)}
        )
        raise e
        
    with transaction.atomic():
        repository.update_password(user, data.new_password)
        
        repository.create_audit_log(
            user=user,
            action="PASSWORD_RESET_SUCCESS",
            ip_address=get_client_ip(request),
            user_agent=get_user_agent(request)
        )
        
    return MessageResponse(message="Password has been reset successfully.")
