"""
Authentication Validation Layer.

This module enforces business rules (e.g., password complexity, email uniqueness).
It throws `ValidationError` or `ConflictError` if rules are violated, ensuring
the Service layer only processes clean data.
"""
import re

from backend.api.auth.repository import get_user_by_email
from backend.core.exceptions import ValidationError, ConflictError


def validate_email_unique(email: str) -> None:
    """
    Checks if an email is already registered.
    Raises ConflictError if it exists.
    """
    if get_user_by_email(email):
        raise ConflictError("A user with this email already exists.")


def validate_password_strength(password: str) -> None:
    """
    Enforces password complexity rules.
    - Minimum 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one number
    - At least one special character
    """
    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters long.")
        
    if not re.search(r"[A-Z]", password):
        raise ValidationError("Password must contain at least one uppercase letter.")
        
    if not re.search(r"[a-z]", password):
        raise ValidationError("Password must contain at least one lowercase letter.")
        
    if not re.search(r"[0-9]", password):
        raise ValidationError("Password must contain at least one number.")
        
    if not re.search(r"[\W_]", password):
        raise ValidationError("Password must contain at least one special character.")


def validate_password_match(password: str, confirm_password: str) -> None:
    """
    Ensures password and confirm_password match.
    """
    if password != confirm_password:
        raise ValidationError("Passwords do not match.")


def validate_registration(data) -> None:
    """
    Orchestrates all validations for a new user registration.
    `data` is expected to be a Pydantic RegisterRequest schema.
    """
    validate_email_unique(data.email)
    validate_password_match(data.password, data.password_confirm)
    validate_password_strength(data.password)
