# Models Used

This document explains the existing database tables that the Authentication Module interacts with. We achieved the complete integration *without creating any new tables*, adhering to the project requirements.

## 1. `User` (Table: `users`)
This is the core authentication model.
- **`id` (UUID):** We use a UUID instead of an integer. This is highly secure (hard to guess) and scales better across distributed databases.
- **`email`:** Replaces the traditional "username". It is marked `unique=True` so two users cannot register with the same email.
- **`password`:** Stores the Argon2 hash. **Never** the plain text.
- **`is_active`:** A boolean flag. If set to `False`, the user is "banned" or "deleted" without actually removing their record from the database (soft delete). The middleware (`AuthBearer`) actively checks this.
- **`is_verified`:** Set to `False` initially. Can be used in V2 for email verification.
- **`last_login`:** Updated every time the user hits the `/login` endpoint.

## 2. `UserProfile` (Table: `user_profiles`)
This stores the user's personal details and app preferences.
- **Relationship:** It has a `OneToOneField` to `User`. This means every `User` has exactly one `UserProfile`.
- **Fields:** `first_name`, `last_name`, `english_level`, `target_language`, etc.
- **Why it's separate:** Separating auth data (email, password) from profile data keeps the auth logic fast and lean. When checking a password, the database only needs to load the small `User` row, not the bulky profile data.

## 3. `AuditLog` (Table: `audit_logs`)
This table records significant system events for security and debugging.
- **Relationship:** A `ForeignKey` to `User` (One-to-Many).
- **`action`:** A string like `"LOGIN_SUCCESS"`, `"REGISTER"`, `"PASSWORD_CHANGED"`.
- **`entity_type` / `entity_id`:** We use `"auth"` for the type and the User's UUID for the ID.
- **`ip_address` & `user_agent`:** Extracted from the HTTP request headers (`core/utils.py`). Invaluable if an account is hacked and we need to trace the attacker.
- **`metadata` (JSONField):** A flexible JSON dictionary. We creatively used this to store the Password Reset Token and its Expiry Date without needing a new database table!
