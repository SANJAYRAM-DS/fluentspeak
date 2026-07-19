# Schemas & Data Validation

This document explains the schema layer in `api/auth/schemas.py`.

## What are Schemas?
In Django Ninja, Schemas are built on top of Pydantic. They serve three critical purposes:
1. **Input Validation:** Automatically checking if the JSON sent by the frontend matches our rules before it ever reaches our service logic.
2. **Type Safety:** Guaranteeing that the data our code processes has the correct Python types (e.g., ensuring `daily_goal_minutes` is an integer).
3. **Serialization:** Converting complex database objects (like the `User` model) into clean JSON responses for the frontend.

## 1. Request Schemas (Input Validation)
These define what the API expects from the client.

### `RegisterRequest`
- **Fields:** `email`, `password`, `password_confirm`, `first_name`, `last_name`
- **Validation:** Uses `EmailStr` to ensure the email format is perfectly valid. The `password` uses `Field(..., min_length=8)` to enforce a minimum length immediately, saving us from checking it manually if it's too short.

### `ChangePasswordRequest`
- Requires the `old_password` to verify the user knows it.
- Enforces the same minimum length constraints on `new_password`.

### `UpdateProfileRequest`
- **Fields:** All fields (`first_name`, `target_language`, etc.) are wrapped in `Optional[...]`.
- **Why:** This allows the frontend to send partial updates. If they only want to update the `timezone`, they just send `{"timezone": "America/New_York"}`, and the other fields remain untouched.

## 2. Response Schemas (Serialization)
These define exactly what the API returns to the client.

### `UserResponse`
- Contains `id`, `email`, `is_verified`, and `created_at`.
- **Security Benefit:** By explicitly defining this schema, we guarantee that sensitive fields like `password` or `is_staff` are *never* accidentally leaked in the JSON response, even if we pass the whole `User` object to the schema.

### `AuthResponse`
- The payload returned upon successful login or registration.
- Combines `TokenResponse` (access + refresh tokens), `UserResponse`, and `ProfileResponse` into a single, cohesive payload. This means the frontend gets everything it needs to log the user in with a single network request.
