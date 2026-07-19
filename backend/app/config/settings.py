"""
Django settings for FluentSpeak project.

Environment variables are loaded from .env file using python-decouple.
All secrets and environment-specific values are externalized.
"""

from pathlib import Path
from datetime import timedelta

from decouple import config, Csv

# =============================================================
# BASE DIRECTORY
# =============================================================
# Points to backend/app/ — where manage.py lives.
# All relative paths in settings resolve from here.

BASE_DIR = Path(__file__).resolve().parent.parent

# =============================================================
# SECURITY
# =============================================================
# SECRET_KEY: Used by Django for cryptographic signing (sessions,
# CSRF tokens, password reset tokens). Must be unique and secret
# in production. Loaded from .env to avoid committing to VCS.

SECRET_KEY = config("SECRET_KEY")

# DEBUG: Never True in production. Controls error pages,
# static file serving, and security checks.

DEBUG = config("DEBUG", default=False, cast=bool)

# ALLOWED_HOSTS: Domains that Django will serve. Prevents
# HTTP Host header attacks. Empty in dev = localhost only.

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="", cast=Csv())

# =============================================================
# INSTALLED APPS
# =============================================================
# Order matters:
# 1. Django built-ins first
# 2. Third-party packages (ninja, corsheaders)
# 3. Project apps last (they depend on the above)

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third-party
    "ninja",
    "rest_framework",
    "corsheaders",
    # Project apps
    "users",
    "topics",
    "scenarios",
    "conversations",
    "vocabulary",
    "ai",
    "analytics",
    "notifications",
]

# =============================================================
# MIDDLEWARE
# =============================================================
# Middleware executes top-to-bottom on requests, bottom-to-top
# on responses. Order is critical:
# - SecurityMiddleware: HTTPS redirects, HSTS headers
# - CorsMiddleware: Must be before CommonMiddleware to handle
#   preflight OPTIONS requests
# - SessionMiddleware: Before AuthenticationMiddleware (auth
#   needs sessions)
# - CsrfViewMiddleware: CSRF protection for form submissions
# - AuthenticationMiddleware: Attaches request.user

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# =============================================================
# URL CONFIGURATION
# =============================================================

ROOT_URLCONF = "config.urls"

# =============================================================
# TEMPLATES
# =============================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# =============================================================
# WSGI / ASGI
# =============================================================

WSGI_APPLICATION = "config.wsgi.application"

# =============================================================
# DATABASE
# =============================================================
# PostgreSQL is used for production-ready features:
# - UUID primary keys
# - JSONField support
# - Transaction isolation
# - Full-text search (future)
#
# All credentials loaded from .env to avoid hardcoding secrets.

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST", default="localhost"),
        "PORT": config("DB_PORT", default="5432"),
    }
}

# =============================================================
# CUSTOM USER MODEL
# =============================================================
# Points to our custom User model that uses email instead of
# username and UUID as primary key. Must be set before first
# migration.

AUTH_USER_MODEL = "users.User"

# =============================================================
# PASSWORD HASHING
# =============================================================
# Argon2 is the PRIMARY hasher — winner of the Password Hashing
# Competition (2015). It is memory-hard, making GPU/ASIC brute-
# force attacks significantly more expensive than bcrypt/PBKDF2.
#
# Django tries hashers top-to-bottom:
# 1. Argon2 — used for all new passwords
# 2. PBKDF2 — fallback for existing passwords (auto-upgrades
#    to Argon2 on next login)
#
# The argon2-cffi package is already in requirements.txt.

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
]

# =============================================================
# PASSWORD VALIDATION
# =============================================================
# Django's built-in validators run during User.set_password()
# and in forms. Our custom validators in api/auth/validators.py
# add additional rules (special chars, uppercase, etc.) at the
# API layer before reaching Django's validators.

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {"min_length": 8},
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# =============================================================
# JWT CONFIGURATION
# =============================================================
# We use PyJWT directly (not simplejwt) for full control over
# token creation and validation with Django Ninja.
#
# JWT_SECRET_KEY: Separate from Django's SECRET_KEY. If Django's
#   SECRET_KEY rotates (e.g., security incident), existing JWTs
#   remain valid. Conversely, we can invalidate all JWTs without
#   affecting Django sessions.
#
# JWT_ALGORITHM: HS256 (HMAC-SHA256) — symmetric signing. The
#   same key signs and verifies. Sufficient for single-server
#   setups. Use RS256 (asymmetric) when multiple services need
#   to verify tokens without the signing key.
#
# ACCESS_TOKEN: Short-lived (15 min). Used for API authorization.
#   If stolen, damage window is small.
#
# REFRESH_TOKEN: Long-lived (7 days). Used only to get new
#   access tokens. Stored securely by the client.

JWT_SECRET_KEY = config("JWT_SECRET_KEY")
JWT_ALGORITHM = config("JWT_ALGORITHM", default="HS256")
JWT_ACCESS_TOKEN_LIFETIME = timedelta(
    minutes=config("JWT_ACCESS_TOKEN_LIFETIME_MINUTES", default=15, cast=int)
)
JWT_REFRESH_TOKEN_LIFETIME = timedelta(
    days=config("JWT_REFRESH_TOKEN_LIFETIME_DAYS", default=7, cast=int)
)

# =============================================================
# PASSWORD RESET
# =============================================================
# How long a password reset token remains valid.

PASSWORD_RESET_TOKEN_EXPIRY_HOURS = config(
    "PASSWORD_RESET_TOKEN_EXPIRY_HOURS", default=1, cast=int
)

# =============================================================
# CORS (Cross-Origin Resource Sharing)
# =============================================================
# In development, allow all origins for convenience.
# In production, replace with explicit allowed origins:
#   CORS_ALLOWED_ORIGINS = ["https://fluentspeak.app"]

CORS_ALLOW_ALL_ORIGINS = config("CORS_ALLOW_ALL_ORIGINS", default=True, cast=bool)

# =============================================================
# REST FRAMEWORK (kept for compatibility)
# =============================================================
# simplejwt config remains for any DRF-based endpoints.
# Our Django Ninja auth uses PyJWT directly.

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=15),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
}

# =============================================================
# INTERNATIONALIZATION
# =============================================================

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# =============================================================
# STATIC FILES
# =============================================================

STATIC_URL = "static/"

# =============================================================
# DEFAULT PRIMARY KEY FIELD TYPE
# =============================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# =============================================================
# RATE LIMITING (Auth)
# =============================================================
# In-memory rate limiting for login attempts.
# MAX_LOGIN_ATTEMPTS: Lock account after N consecutive failures.
# LOGIN_LOCKOUT_MINUTES: How long the lockout lasts.
# In production, use Redis-backed rate limiting instead.

MAX_LOGIN_ATTEMPTS = config("MAX_LOGIN_ATTEMPTS", default=5, cast=int)
LOGIN_LOCKOUT_MINUTES = config("LOGIN_LOCKOUT_MINUTES", default=15, cast=int)