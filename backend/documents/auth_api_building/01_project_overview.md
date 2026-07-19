# Project Overview: Authentication Module V1

Welcome to Phase 1 of building the FluentSpeak Authentication Module! This document provides a high-level overview of the entire authentication architecture we are building.

## Why is Authentication Needed?
Authentication is the process of verifying who a user is. For FluentSpeak:
1. **User Identity:** We need to know who is taking language lessons, tracking their vocabulary, and completing scenarios.
2. **Data Security:** Users should only be able to access their own profiles, progress, and conversation histories.
3. **Audit Trails:** We need to log critical events (like logins or password resets) for security monitoring.

## How the Authentication Architecture Works
We are using **JSON Web Tokens (JWT)** for stateless authentication. Here's why:
- **Statelessness:** The server does not need to store session data in the database. All the information needed to verify the user is contained within the token itself. This makes the API highly scalable.
- **Client-Side Storage:** The client (web browser, mobile app) stores the token and sends it with every protected request.

### Access vs. Refresh Tokens
We use a two-token system for optimal security and user experience:
1. **Access Token (Short-lived - 15 minutes):** 
   - This token is sent with every API request via the `Authorization: Bearer <token>` header.
   - It contains the user's ID (`sub`) and email.
   - If a malicious actor steals this token, they only have access for a maximum of 15 minutes.
2. **Refresh Token (Long-lived - 7 days):**
   - This token is *only* used to request a new Access Token when the old one expires.
   - It is kept secure by the client (usually in HttpOnly cookies or secure local storage).
   - If the user logs out, they simply delete this token on the client side.

## How the Request Flows
1. **Login:** The user sends their email and password to `/api/auth/login`.
2. **Verification:** The Auth Service verifies the credentials against the database (using Argon2 to hash the provided password and compare it).
3. **Token Issuance:** If valid, the system generates an Access Token and a Refresh Token and returns them.
4. **Subsequent Requests:** The client attaches the Access Token to the `Authorization` header of future requests (e.g., `GET /api/auth/me`).
5. **Validation:** Django Ninja's `HttpBearer` middleware intercepts the request, decodes the JWT, verifies the signature, and fetches the user from the database. It then attaches the user to the `request` object.
6. **Processing:** The API endpoint processes the request, knowing exactly who the user is (`request.auth`).

## How Django Ninja Fits In
Django Ninja is a fast, async-ready web framework for building APIs with Django and Python 3.6+ type hints.
- **Validation:** It automatically validates incoming JSON payloads using Pydantic schemas.
- **Routing:** It provides a clean, FastAPI-like router system for defining endpoints.
- **Authentication:** It provides built-in mechanisms (like `HttpBearer`) to protect specific routes, making it very easy to integrate our JWT logic.

This architecture ensures that our API remains fast, secure, and easy to scale!
