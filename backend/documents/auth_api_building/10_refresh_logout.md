# Refresh & Logout APIs

## 1. Refresh Token Flow (`POST /api/auth/refresh`)

When an Access Token expires (after 15 minutes), the client must obtain a new one.

1. **Client Sends Refresh Token:** `{"refresh": "eyJhb..."}`
2. **Decode & Validate:** `jwt.decode_token(token, token_type="refresh")`.
   - If the token is actually an access token, it raises an error.
   - If the token is expired (older than 7 days), the user is forced to log in again.
3. **Fetch User:** We extract `sub` (user_id) from the payload and check the DB. If the user was banned (`is_active=False`) *while* they held this token, we reject them here!
4. **Audit Log:** We log `"TOKEN_REFRESH"`.
5. **Issue New Pair:** We generate a *new* Access Token AND a *new* Refresh Token (Refresh Token Rotation).
6. **Response:** Return both tokens.

## 2. Logout Flow (`POST /api/auth/logout`)

Our JWT architecture is **stateless**. The server does not store active tokens in a database table. Therefore, to log out:
1. **Client Action:** The client (browser/app) simply deletes the Access and Refresh tokens from its local storage.
2. **Server Action:** The client hits the `/logout` endpoint (requires authentication). The server does *not* need to blacklist the token (in V1). It simply records a `"LOGOUT"` event in the `AuditLog` so we have a record of when the user intentionally ended their session.

*Note on Stateless JWT limitations:* Because we don't blacklist tokens in V1, if an access token is stolen, it remains valid until it naturally expires (15 min). This is why access tokens must be short-lived.
