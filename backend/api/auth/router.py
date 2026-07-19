"""
Authentication Router.

Maps HTTP endpoints to service layer functions.
Views are kept intentionally thin — they only handle HTTP semantics.
"""
from ninja import Router
from django.http import HttpRequest

from backend.api.auth import service
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
from backend.core.permissions import AuthBearer

# Router instance
router = Router(tags=["Authentication"])

# Reusable security schema for protected routes
auth_bearer = AuthBearer()


@router.post("/register", response={201: AuthResponse}, auth=None)
def register_user(request: HttpRequest, payload: RegisterRequest):
    """
    Register a new user account.
    """
    return 201, service.register(payload, request)


@router.post("/login", response=AuthResponse, auth=None)
def login_user(request: HttpRequest, payload: LoginRequest):
    """
    Authenticate and receive access and refresh tokens.
    """
    return service.login(payload, request)


@router.post("/refresh", response=TokenResponse, auth=None)
def refresh_token(request: HttpRequest, payload: RefreshTokenRequest):
    """
    Exchange a valid refresh token for a new pair of access/refresh tokens.
    """
    return service.refresh_token(payload, request)


@router.post("/logout", response=MessageResponse, auth=auth_bearer)
def logout_user(request: HttpRequest):
    """
    Log out the current user (audit logging).
    Client must discard the token.
    """
    return service.logout(request.auth, request)


@router.get("/me", response=CurrentUserResponse, auth=auth_bearer)
def get_current_user(request: HttpRequest):
    """
    Get the currently authenticated user's details and profile.
    """
    return service.get_current_user(request.auth)


@router.put("/profile", response=CurrentUserResponse, auth=auth_bearer)
def update_profile(request: HttpRequest, payload: UpdateProfileRequest):
    """
    Update the authenticated user's profile.
    """
    return service.update_profile(request.auth, payload)


@router.post("/change-password", response=MessageResponse, auth=auth_bearer)
def change_password(request: HttpRequest, payload: ChangePasswordRequest):
    """
    Change the authenticated user's password.
    """
    return service.change_password(request.auth, payload, request)


@router.post("/forgot-password", response=MessageResponse, auth=None)
def forgot_password(request: HttpRequest, payload: ForgotPasswordRequest):
    """
    Request a password reset link (token).
    """
    return service.forgot_password(payload, request)


@router.post("/reset-password", response=MessageResponse, auth=None)
def reset_password(request: HttpRequest, payload: ResetPasswordRequest):
    """
    Reset password using a token.
    """
    return service.reset_password(payload, request)
