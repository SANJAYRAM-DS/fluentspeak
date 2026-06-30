import uuid

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        UserProfile.objects.get_or_create(user=user)
        UserProgress.objects.get_or_create(user=user)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_verified", True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    password = models.TextField(db_column="password_hash")
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    full_name = models.CharField(max_length=100, blank=True)
    avatar_url = models.TextField(blank=True)
    level = models.CharField(max_length=20, default="beginner")
    daily_goal = models.IntegerField(default=10)
    timezone = models.CharField(max_length=100, default="UTC")

    class Meta:
        db_table = "user_profiles"

    def __str__(self):
        return self.full_name or self.user.email


class UserProgress(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="progress",
    )
    conversations_completed = models.IntegerField(default=0)
    words_learned = models.IntegerField(default=0)
    current_streak = models.IntegerField(default=0)
    total_minutes = models.IntegerField(default=0)

    class Meta:
        db_table = "user_progress"

    def __str__(self):
        return f"{self.user.email} progress"
