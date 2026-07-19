"""
Security utilities: Password hashing, verification, and token generation.
"""
import secrets
from django.contrib.auth.hashers import make_password, check_password


def hash_password(raw_password: str) -> str:
    """
    Hashes a raw password using Django's default hasher (configured
    as Argon2 in settings.py).
    
    Returns the hashed string formatted for database storage.
    """
    return make_password(raw_password)


def verify_password(raw_password: str, hashed_password: str) -> bool:
    """
    Verifies a raw password against its stored hash.
    
    Returns True if the password matches, False otherwise.
    """
    return check_password(raw_password, hashed_password)


def generate_reset_token() -> str:
    """
    Generates a cryptographically secure, URL-safe random string.
    Used for password resets, email verification, etc.
    
    Provides ~256 bits of entropy.
    """
    return secrets.token_urlsafe(32)
