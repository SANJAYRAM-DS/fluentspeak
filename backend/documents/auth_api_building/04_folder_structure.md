# Folder Structure

This document explains the organization of the authentication module files, their responsibilities, and how they depend on each other.

Our architecture strictly separates concerns.

## `core/` (The Engine)
These files provide foundation logic that is independent of any specific API endpoint.

- **`core/exceptions.py`**: Defines custom error classes (`AuthenticationError`, `ValidationError`). 
  - *Why:* Instead of returning hardcoded HTTP responses scattered across the code, we raise an exception. The router catches it and formats a standard JSON response.
- **`core/utils.py`**: Helper functions like `get_client_ip()` and `get_user_agent()`.
  - *Why:* Keeps the main business logic clean and DRY (Don't Repeat Yourself).
- **`core/security.py`**: Wraps Django's Argon2 hasher and token generation.
  - *Why:* Abstracting security logic means if we ever change hashing algorithms, we only update this one file.
- **`core/jwt.py`**: Logic for encoding and decoding tokens using `PyJWT`.
  - *Why:* Centralizes the token logic, payload structure, and expiration checking.
- **`core/permissions.py`**: Contains the `AuthBearer` class.
  - *Why:* This is the gatekeeper middleware. It sits in front of protected routes, intercepts requests, and uses `core/jwt.py` to validate tokens.

## `api/auth/` (The Module)
This is where the actual authentication feature lives.

- **`repository.py`**: The Data Layer. 
  - *Responsibility:* ALL database queries live here (creating users, finding emails, inserting audit logs).
  - *Rule:* Views and services must *never* call `User.objects` directly. They ask the repository.
- **`validators.py`**: The Validation Layer.
  - *Responsibility:* Checks business rules (password strength, email format).
- **`schemas.py`**: The Contract Layer.
  - *Responsibility:* Pydantic models defining exactly what JSON the API expects as input, and what JSON it promises to output.
- **`service.py`**: The Business Logic Layer.
  - *Responsibility:* The core brain. It receives validated data from the router, uses the repository to fetch/save data, uses validators to enforce rules, and returns results.
- **`router.py`**: The Routing Layer (Views).
  - *Responsibility:* Purely HTTP handling. It maps URLs (e.g., `POST /login`) to service functions. It should be very "thin" (no business logic).
