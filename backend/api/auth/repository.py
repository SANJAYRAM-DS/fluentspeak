"""
Authentication Repository.

This module encapsulates all database interactions related to authentication.
Services MUST use these functions instead of calling Django ORM directly.
This separates database logic from business logic.
"""
from typing import Optional
from datetime import datetime, timezone, timedelta
from django.utils import timezone as django_timezone

from backend.app.users.models import User, UserProfile
from backend.app.analytics.models import AuditLog
from backend.core.security import hash_password
from django.conf import settings


def get_user_by_email(email: str) -> Optional[User]:
    """Fetch a user by their email address."""
    return User.objects.filter(email=email).first()


def get_user_by_id(user_id: str) -> Optional[User]:
    """Fetch a user by their UUID."""
    return User.objects.filter(id=user_id).first()


def create_user(email: str, password: str) -> User:
    """
    Creates a new user with a hashed password.
    Note: We do not use user.set_password here because we are explicitly
    hashing it at the service layer/using our custom hash_password.
    Actually, to maintain Django compatibility, we can use the custom User manager.
    """
    user = User.objects.create_user(
        email=email,
        password=password
    )
    return user


def create_user_profile(user: User, first_name: str = "", last_name: str = "") -> UserProfile:
    """Creates a UserProfile associated with the given user."""
    return UserProfile.objects.create(
        user=user,
        first_name=first_name,
        last_name=last_name
    )


def update_user_profile(user: User, update_data: dict) -> UserProfile:
    """Updates the user's profile with provided fields."""
    profile = user.profile
    for field, value in update_data.items():
        setattr(profile, field, value)
    profile.save()
    return profile


def update_last_login(user: User) -> None:
    """Updates the user's last_login timestamp to now."""
    user.last_login = django_timezone.now()
    user.save(update_fields=["last_login"])


def update_password(user: User, raw_password: str) -> None:
    """
    Hashes the new password and updates the user record.
    """
    user.set_password(raw_password)
    user.save(update_fields=["password"])


def create_audit_log(
    user: Optional[User],
    action: str,
    ip_address: str = "",
    user_agent: str = "",
    metadata: dict = None
) -> AuditLog:
    """
    Creates an audit log entry for security events.
    """
    return AuditLog.objects.create(
        user=user,
        action=action,
        entity_type="auth",
        entity_id=user.id if user else None,
        ip_address=ip_address,
        user_agent=user_agent,
        metadata=metadata or {}
    )


def save_reset_token(user: User, token: str) -> None:
    """
    Saves a password reset token for a user.
    Since we cannot create a new table, we store it in the AuditLog metadata.
    """
    expiry_hours = getattr(settings, "PASSWORD_RESET_TOKEN_EXPIRY_HOURS", 1)
    expiry = datetime.now(timezone.utc) + timedelta(hours=expiry_hours)
    
    metadata = {
        "reset_token": token,
        "expires_at": expiry.isoformat()
    }
    
    create_audit_log(
        user=user,
        action="PASSWORD_RESET_REQUESTED",
        metadata=metadata
    )


def get_user_by_reset_token(token: str) -> Optional[User]:
    """
    Finds a user by an active password reset token stored in the audit logs.
    """
    # Find the most recent PASSWORD_RESET_REQUESTED log that contains this token
    log = AuditLog.objects.filter(
        action="PASSWORD_RESET_REQUESTED",
        metadata__reset_token=token
    ).order_by("-created_at").first()

    if not log or not log.user:
        return None

    # Check expiration
    expires_at_str = log.metadata.get("expires_at")
    if not expires_at_str:
        return None
        
    try:
        expires_at = datetime.fromisoformat(expires_at_str)
        if datetime.now(timezone.utc) > expires_at:
            return None  # Token expired
    except ValueError:
        return None
        
    return log.user
