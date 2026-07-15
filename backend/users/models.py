import uuid

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)

from .managers import UserManager


class EnglishLevel(models.TextChoices):
    A1 = "A1", "A1"
    A2 = "A2", "A2"
    B1 = "B1", "B1"
    B2 = "B2", "B2"
    C1 = "C1", "C1"
    C2 = "C2", "C2"


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom authentication model.
    Email is used instead of username.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    email = models.EmailField(
        unique=True,
        max_length=255
    )

    is_active = models.BooleanField(
        default=True
    )

    is_verified = models.BooleanField(
        default=False
    )

    is_staff = models.BooleanField(
        default=False
    )

    last_login = models.DateTimeField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    objects = UserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []

    class Meta:
        db_table = "users"
        ordering = ["-created_at"]

    def __str__(self):
        return self.email


class UserProfile(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    first_name = models.CharField(
        max_length=100,
        blank=True
    )

    last_name = models.CharField(
        max_length=100,
        blank=True
    )

    avatar_url = models.TextField(
        blank=True
    )

    english_level = models.CharField(
        max_length=20,
        choices=EnglishLevel.choices,
        default=EnglishLevel.A1
    )

    native_language = models.CharField(
        max_length=50,
        blank=True
    )

    target_language = models.CharField(
        max_length=50,
        default="English"
    )

    daily_goal_minutes = models.PositiveIntegerField(
        default=15
    )

    timezone = models.CharField(
        max_length=100,
        default="UTC"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "user_profiles"
        ordering = ["first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}".strip() or self.user.email