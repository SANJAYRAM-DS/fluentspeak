# Dependencies & Installation

This document explains every package we use for the authentication module, why we need it, how to install it, and common pitfalls.

All of these are already in your `requirements.txt`. If you were building this from scratch, you would run the installation commands provided.

## 1. Django & Django Ninja
**Installation:** `pip install Django django-ninja`
- **Purpose:** The core framework and API routing layer.
- **Why we need it:** Django provides the robust ORM (Object-Relational Mapping), migration system, and security middleware. Django Ninja adds fast, type-hinted API routing and automatic validation.
- **Common Mistakes:** Forgetting to add `"ninja"` to `INSTALLED_APPS` in `settings.py`.

## 2. PyJWT
**Installation:** `pip install PyJWT`
- **Purpose:** Creating and decoding JSON Web Tokens.
- **Why we need it:** We use this to manually create access and refresh tokens. While `djangorestframework_simplejwt` is installed, it is heavily tied to DRF views. Using `PyJWT` directly gives us absolute control over the token lifecycle within Django Ninja.
- **Alternatives:** `python-jose` (also good, but PyJWT is standard and lightweight).

## 3. Argon2 (argon2-cffi)
**Installation:** `pip install argon2-cffi`
- **Purpose:** Password hashing.
- **Why we need it:** Django uses PBKDF2 by default, which is okay, but Argon2 is the winner of the Password Hashing Competition. It is memory-hard, meaning it protects against GPU brute-force attacks much better than PBKDF2 or bcrypt.
- **Configuration:** We added it to `PASSWORD_HASHERS` in `settings.py` so Django automatically uses it when we call `user.set_password()`.
- **Common Mistakes:** Installing it but forgetting to update `PASSWORD_HASHERS` in `settings.py`.

## 4. Python Decouple
**Installation:** `pip install python-decouple`
- **Purpose:** Environment variable management.
- **Why we need it:** Hardcoding secrets (like `SECRET_KEY` or database passwords) in `settings.py` is a massive security risk. `python-decouple` reads variables from a `.env` file, allowing us to keep secrets out of version control.
- **Alternatives:** `python-dotenv` (also installed, but `decouple` provides nice casting features like `cast=bool`).

## 5. Pydantic
**Installation:** `pip install pydantic pydantic-settings email-validator`
- **Purpose:** Data validation and schema definition.
- **Why we need it:** Django Ninja uses Pydantic under the hood. We define our request/response schemas (like `RegisterRequest`) as Pydantic models. It automatically handles type checking and validation (e.g., ensuring an email is actually an email via `email-validator`).

## 6. PostgreSQL (psycopg2-binary)
**Installation:** `pip install psycopg2-binary`
- **Purpose:** Database adapter for PostgreSQL.
- **Why we need it:** SQLite (the default) is not suitable for production. We use PostgreSQL because it handles concurrent connections better and supports advanced features like UUID primary keys natively.

## How it integrates into the project
These dependencies form the foundation. Django handles the DB, Django Ninja handles the API endpoints, Pydantic validates the incoming data, PyJWT creates the tokens, Argon2 secures the passwords, and Python Decouple keeps the configuration secure.
