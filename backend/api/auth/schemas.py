"""
Authentication Schemas.

Pydantic schemas used by Django Ninja for request validation and response serialization.
"""
from typing import Optional
from ninja import Schema
from pydantic import EmailStr, Field
import uuid


# ==========================================
# REQUEST SCHEMAS
# ==========================================

class RegisterRequest(Schema):
    email: EmailStr
    password: str = Field(..., min_length=8, description="Must contain uppercase, lowercase, number, and special character")
    password_confirm: str = Field(..., min_length=8)
    first_name: Optional[str] = ""
    last_name: Optional[str] = ""


class LoginRequest(Schema):
    email: EmailStr
    password: str


class RefreshTokenRequest(Schema):
    refresh: str = Field(..., description="The long-lived refresh token")


class ChangePasswordRequest(Schema):
    old_password: str
    new_password: str = Field(..., min_length=8)
    new_password_confirm: str = Field(..., min_length=8)


class ForgotPasswordRequest(Schema):
    email: EmailStr


class ResetPasswordRequest(Schema):
    token: str
    new_password: str = Field(..., min_length=8)
    new_password_confirm: str = Field(..., min_length=8)


class UpdateProfileRequest(Schema):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    english_level: Optional[str] = None
    native_language: Optional[str] = None
    target_language: Optional[str] = None
    daily_goal_minutes: Optional[int] = None
    timezone: Optional[str] = None


# ==========================================
# RESPONSE SCHEMAS
# ==========================================

class MessageResponse(Schema):
    """Generic success/error message response."""
    message: str


class TokenResponse(Schema):
    access: str
    refresh: str


class UserResponse(Schema):
    id: uuid.UUID
    email: str
    is_verified: bool
    created_at: str
    
    @staticmethod
    def resolve_created_at(obj):
        return obj.created_at.isoformat() if obj.created_at else None


class ProfileResponse(Schema):
    first_name: str
    last_name: str
    avatar_url: str
    english_level: str
    native_language: str
    target_language: str
    daily_goal_minutes: int
    timezone: str
    onboarding_completed: bool


class CurrentUserResponse(Schema):
    """Response returned when fetching the current user."""
    user: UserResponse
    profile: ProfileResponse


class AuthResponse(Schema):
    """Response returned after successful login or registration."""
    tokens: TokenResponse
    user: UserResponse
    profile: ProfileResponse
