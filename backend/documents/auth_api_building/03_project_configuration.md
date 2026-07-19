# Project Configuration

This document explains the critical configuration changes made in `settings.py` and the `.env` file to support our authentication architecture.

## 1. Environment Variables (`.env`)
We created a `.env` file in the same directory as `settings.py`. This file is ignored by Git (via `.gitignore`).

**Why this exists:** To prevent sensitive information from leaking into source control.

Key variables added:
- `SECRET_KEY`: Django's internal cryptographic key.
- `JWT_SECRET_KEY`: A separate key specifically for signing JSON Web Tokens. By keeping this separate, we can rotate Django's key without invalidating active user sessions.
- Database Credentials (`DB_NAME`, `DB_USER`, `DB_PASSWORD`): Keeps production credentials secure.

## 2. `settings.py` Changes

### Secrets and Decouple
We imported `config` from `decouple` to read our `.env` file:
```python
SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", default=False, cast=bool)
```

### Password Hashers
We updated Django to use Argon2 as the primary password hasher:
```python
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
]
```
**Why:** When `user.set_password()` is called, Django uses the first hasher in this list. Argon2 provides state-of-the-art protection against brute-force attacks.

### JWT Configuration
We added specific constants for our token logic:
```python
JWT_SECRET_KEY = config("JWT_SECRET_KEY")
JWT_ALGORITHM = config("JWT_ALGORITHM", default="HS256")
JWT_ACCESS_TOKEN_LIFETIME = timedelta(minutes=15)
JWT_REFRESH_TOKEN_LIFETIME = timedelta(days=7)
```
**Why:** Centralizing these settings makes it easy to adjust session lengths globally. The 15-minute access token minimizes the risk window if a token is stolen.

### Custom User Model
```python
AUTH_USER_MODEL = "users.User"
```
**Why:** Tells Django to use our custom User model (which uses UUIDs and email for login) instead of the default username-based model.

### CORS Configuration
```python
CORS_ALLOW_ALL_ORIGINS = True  # Or read from config
```
**Why:** Allows the frontend application (which might run on a different port like localhost:3000 during development) to make API requests to our Django backend without being blocked by the browser's Same-Origin Policy.

## 3. The `MIDDLEWARE` Bug Fix
The existing project had a typo where `MIDDLEWARE` was defined as a list within a list:
```python
MIDDLEWARE = [
    MIDDLEWARE = [ ... ]
]
```
This was corrected. Middleware order is critical for security: `SecurityMiddleware` must run first, `CorsMiddleware` must run before `CommonMiddleware`, and `AuthenticationMiddleware` must run after `SessionMiddleware`.
