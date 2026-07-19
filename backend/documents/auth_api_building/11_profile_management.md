# Profile & Password Management

This document explains the endpoints used by authenticated users to manage their accounts, and the public endpoints for recovering a lost account.

## 1. Current User (`GET /api/auth/me`)
- **Protection:** Requires `Authorization: Bearer <token>`.
- **Flow:** The `AuthBearer` middleware automatically decodes the token, fetches the user, and attaches it to `request.auth`. The endpoint simply returns `service.get_current_user(request.auth)`, serialized by `CurrentUserResponse`.

## 2. Update Profile (`PUT /api/auth/profile`)
- **Protection:** Requires token.
- **Flow:** The client sends an `UpdateProfileRequest`. Any field omitted is ignored (thanks to `exclude_unset=True` in Pydantic). The service loops through the provided fields, updates the `UserProfile` object, and saves it.

## 3. Change Password (`POST /api/auth/change-password`)
- **Protection:** Requires token (user must be logged in).
- **Flow:** 
  1. Validates that the user provided the correct `old_password`.
  2. Enforces complexity rules on `new_password`.
  3. Updates the database and logs a `"PASSWORD_CHANGED"` event.
- **Security:** Requires old password so that if a user leaves their device unlocked, a malicious person cannot easily lock them out of their own account.

## 4. Forgot Password (`POST /api/auth/forgot-password`)
- **Protection:** Public.
- **Flow:**
  1. Checks if the email exists.
  2. Generates a secure random 32-byte token (`secrets.token_urlsafe(32)`).
  3. Creates an `AuditLog` entry of type `"PASSWORD_RESET_REQUESTED"` and stores the token + a 1-hour expiry timestamp in the `metadata` JSON field.
  4. Returns the token in the response (for V1 testing purposes).

## 5. Reset Password (`POST /api/auth/reset-password`)
- **Protection:** Public (requires the token from step 4).
- **Flow:**
  1. Searches the `AuditLog` for an unexpired `"PASSWORD_RESET_REQUESTED"` event containing the provided token.
  2. If found, it retrieves the associated User.
  3. Enforces complexity on the new password.
  4. Updates the password and logs `"PASSWORD_RESET_SUCCESS"`.
