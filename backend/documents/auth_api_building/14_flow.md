# The Master Flow

This is the most important document. It explains exactly how a request travels through the system from start to finish, and provides the blueprint for how you can modify this code months from now without breaking anything.

## The Complete End-to-End Request Lifecycle

Let's trace a `POST /api/auth/login` request.

1. **The Entry Point (`config/urls.py`):**
   - Django receives the HTTP request.
   - It checks `urls.py` and sees that `/api/` is delegated to `api.urls`.
2. **The API Registration (`api/api.py`):**
   - `api.urls` points to the `NinjaAPI` instance defined in `api/api.py`.
   - The Ninja instance knows that `/auth/` is handled by our `auth_router`.
3. **The Router (`api/auth/router.py`):**
   - The router matches the `/login` path.
   - **Crucial Step:** Before running the view function, Django Ninja intercepts the raw JSON body and pushes it through the `LoginRequest` Pydantic schema defined in `api/auth/schemas.py`.
   - If the JSON is missing an email, Ninja immediately returns a `422 Validation Error`.
4. **The Service Layer (`api/auth/service.py`):**
   - The router passes the validated `LoginRequest` object to `service.login()`.
   - The service asks the repository: "Give me the user with this email."
5. **The Repository Layer (`api/auth/repository.py`):**
   - The repository executes `User.objects.filter(email=email).first()` and returns the user object (or None).
6. **The Security Layer (`core/security.py`):**
   - The service passes the raw password and the database hash to `verify_password()`.
   - It uses Argon2 to check if they match.
7. **Audit & Token Generation (`core/jwt.py`):**
   - The service asks the repository to update `last_login` and create a `LOGIN_SUCCESS` audit log.
   - The service asks `jwt.create_token_pair()` for access and refresh tokens.
8. **The Response (`api/auth/schemas.py`):**
   - The service returns the data.
   - The router takes the data and pushes it through the `AuthResponse` schema.
   - The schema automatically strips out any sensitive internal fields and formats it as clean JSON.
   - The client receives the `200 OK` response.

## How to safely modify authentication features later

If you need to change this system months from now, follow these rules based on the architecture:

**Scenario 1: You want to add a new field to registration (e.g., "phone_number")**
1. Add the field to the `UserProfile` model in `models.py` and run migrations.
2. Add `phone_number` to `RegisterRequest` in `schemas.py`.
3. Update `repository.create_user_profile()` to accept and save the phone number.
4. Update `service.register()` to pass the phone number from the payload to the repository.

**Scenario 2: You want to change password complexity rules**
1. Do not touch the router, service, or schemas.
2. Open `api/auth/validators.py`.
3. Modify `validate_password_strength()`.

**Scenario 3: You want to change the JWT expiration time**
1. Open the `.env` file and change `JWT_ACCESS_TOKEN_LIFETIME_MINUTES`.
2. No code changes required.

**Scenario 4: You want to log a new type of event**
1. Open `api/auth/service.py`.
2. Find the relevant function and add a call to `repository.create_audit_log(..., action="NEW_EVENT_NAME")`.

By strictly respecting these layers (Router -> Schema -> Validator -> Service -> Repository), the code remains modular, testable, and highly maintainable.
