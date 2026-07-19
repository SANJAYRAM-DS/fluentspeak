# Security Implementation

This document details the specific security measures implemented in our Authentication Module.

## 1. Password Hashing (Argon2)
**What it is:** Argon2 is the winner of the 2015 Password Hashing Competition.
**Implementation:** `core/security.py`
**Why it's secure:**
- **Memory-Hard:** Unlike older algorithms (MD5, SHA-256) or even bcrypt, Argon2 requires a configurable amount of RAM to compute. This makes it incredibly expensive and slow for attackers to use GPUs (Graphics Processing Units) or custom ASIC chips to brute-force crack stolen passwords.
- **Salting:** Django automatically generates a unique salt for every password, neutralizing "rainbow table" attacks.

## 2. JSON Web Tokens (JWT)
**Implementation:** `core/jwt.py`
**Why it's secure:**
- **Stateless Verification:** The token is digitally signed using HMAC-SHA256 (`HS256`) and the `JWT_SECRET_KEY` from our `.env` file. We do not need to look up the token in the database to know it is valid; the cryptographic signature proves it wasn't tampered with.
- **Damage Control (Short Expiry):** Access tokens expire in 15 minutes. If an attacker intercepts a token (e.g., via a compromised Wi-Fi network), their window of opportunity is very small.

## 3. Refresh Tokens (Current State)
**Implementation:** Handled via the `/auth/refresh` endpoint.
**Current Architecture (Version 1):** 
- Refresh tokens are long-lived (7 days) and are used to request new access tokens.
- **Rotation is NOT currently implemented**. When a refresh token is used, a new one is generated, but the old refresh token remains valid until its 7-day expiration.
- **Security Implications:** If an attacker steals a refresh token, they can continually generate new access tokens for 7 days. This is an accepted trade-off for the MVP to minimize database statefulness.
- **V2 Roadmap:** Implement a Token Blacklist (or Token Versioning on the User model) to immediately invalidate old refresh tokens when a new one is issued, effectively implementing strict Refresh Token Rotation.

## 4. Middleware Protection (`AuthBearer`)
**Implementation:** `core/permissions.py`
**How it works:** 
1. Client sends `Authorization: Bearer eyJhb...`
2. Django Ninja triggers `AuthBearer.authenticate()`.
3. The token is decoded and signature verified.
4. The system explicitly checks the `type` claim to ensure a user isn't trying to use a "refresh" token as an "access" token (a common JWT vulnerability).
5. The system queries the database to ensure the user still exists and `is_active=True`. Even if the token hasn't expired, a disabled user will be immediately rejected.

## 5. Timing Attack Mitigation
**Implementation:** `api/auth/service.py` (in `forgot_password`)
**Why it's secure:**
When an attacker tries to guess registered emails via the `/forgot-password` endpoint, the system responds identically whether the email exists or not. However, hashing algorithms (Argon2) take a measurable amount of CPU time (~300ms). If we only hashed passwords for *existing* users, an attacker could measure the response time:
- Fast response (10ms) = Email doesn't exist.
- Slow response (300ms) = Email exists.
**Fix:** If the user is not found, we explicitly perform a dummy hash (`hash_password("dummy")`) to normalize the response time.

## 6. Audit Logging
- Every critical authentication action (Register, Login, Password Change, Token Refresh, and Logout) is logged in the `AuditLog` table.
- We explicitly trap failed attempts (`_FAILED` suffix) in the service layer using `try/except` blocks and log them by `ip_address` to allow for rate limiting and forensic analysis without needing an authenticated `User` object.
