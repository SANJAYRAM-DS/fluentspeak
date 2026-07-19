"""
JSON Web Token (JWT) management.

This module handles the manual creation, decoding, and validation
of access and refresh tokens using PyJWT.
"""
import jwt
from datetime import datetime, timezone
from typing import Dict, Any

from django.conf import settings

from backend.app.users.models import User
from backend.core.exceptions import AuthenticationError


def create_access_token(user: User) -> str:
    """
    Creates a short-lived access token for API authorization.
    """
    now = datetime.now(timezone.utc)
    expiry = now + settings.JWT_ACCESS_TOKEN_LIFETIME
    
    payload = {
        "sub": str(user.id),
        "email": user.email,
        "type": "access",
        "iat": now.timestamp(),
        "exp": expiry.timestamp()
    }
    
    return jwt.encode(
        payload, 
        settings.JWT_SECRET_KEY, 
        algorithm=settings.JWT_ALGORITHM
    )


def create_refresh_token(user: User) -> str:
    """
    Creates a long-lived refresh token used only to obtain
    new access tokens.
    """
    now = datetime.now(timezone.utc)
    expiry = now + settings.JWT_REFRESH_TOKEN_LIFETIME
    
    payload = {
        "sub": str(user.id),
        "type": "refresh",
        "iat": now.timestamp(),
        "exp": expiry.timestamp()
    }
    
    return jwt.encode(
        payload, 
        settings.JWT_SECRET_KEY, 
        algorithm=settings.JWT_ALGORITHM
    )


def create_token_pair(user: User) -> Dict[str, str]:
    """
    Creates and returns both access and refresh tokens for a user.
    """
    return {
        "access": create_access_token(user),
        "refresh": create_refresh_token(user)
    }


def decode_token(token: str, token_type: str = "access") -> Dict[str, Any]:
    """
    Decodes and validates a JWT.
    
    Checks the signature, expiration time, and token type.
    Raises AuthenticationError if validation fails.
    """
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM]
        )
        
        # Verify token type (don't allow refresh tokens to be used as access tokens)
        if payload.get("type") != token_type:
            raise AuthenticationError(f"Invalid token type. Expected '{token_type}' token.")
            
        return payload
        
    except jwt.ExpiredSignatureError:
        raise AuthenticationError("Token has expired. Please log in again.")
    except jwt.InvalidTokenError:
        raise AuthenticationError("Invalid token. Please log in again.")
