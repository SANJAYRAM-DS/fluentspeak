# Topics Module: Validation & Security

This document covers the security practices and validation logic implemented in `backend/api/topics/validators.py`.

## 1. Input Validation
All parameters passed via URLs or query strings are first captured by Pydantic schemas, which provide type coercion. However, we employ explicit Python functions to throw standard `ValidationError` or `NotFoundError` exceptions to strictly control the error messages and HTTP status codes.

### UUID Validation
- **Risk**: A malformed string sent in `GET /api/v1/topics/{topic_id}` can crash the database driver.
- **Solution**: `validate_uuid` attempts to parse the string into a Python `uuid.UUID` object. If it fails (ValueError, TypeError), we catch it and raise a `NotFoundError` (404), ensuring we meet the edge case requirement: `Invalid UUID -> 404`.

### Pagination Validation
- **Risk**: Extreme `limit` values (e.g., `limit=1000000`) can cause database denial of service (DoS) and out-of-memory errors.
- **Solution**: `validate_pagination` strictly enforces `page >= 1` and `limit <= 100`. If violated, a `400 Bad Request` is returned.

### Ordering Validation
- **Risk**: Exposing ordering to the frontend can allow an attacker to order by internal boolean flags (e.g., `is_active`) or perform SQL injection via `ORDER BY`.
- **Solution**: `validate_topic_ordering` uses an explicit whitelist: `['display_order', 'title', 'difficulty']`. Any other string immediately triggers a 400 error.

## 2. Search Sanitization & SQL Injection Prevention
- **Risk**: A malicious user sends `?search=' OR 1=1--` attempting to retrieve unauthorized data, or sends a 10MB string to exhaust CPU during regex/database search.
- **Solution**: `sanitize_search` performs two checks:
  1. Truncates/Rejects searches longer than 100 characters.
  2. Uses regex `re.sub(r'[^\w\s\-.,?]', '', search)` to strip dangerous characters like single quotes, double quotes, semicolons, and parentheses.
  3. The Django ORM inherently protects against SQL injection when using `.filter(title__icontains=search)`, because it parameterizes the queries at the driver level (psycopg2).

## 3. XSS Prevention
- **Risk**: A user manages to inject `<script>alert(1)</script>` into the search, and the API reflects this in the response.
- **Solution**: Django Ninja strictly formats JSON responses. The `Content-Type` is forced to `application/json`, which modern browsers will not execute as HTML/JavaScript. We never return unescaped HTML content.

## 4. Error Handling Strategy
We use custom exceptions defined in `backend/core/exceptions.py`. These exceptions inherit from a base class that the global `api.py` catches. This guarantees:
- No internal stack traces (500 errors) are ever exposed to the user for validation failures.
- The API always returns a consistent `{"message": "..."}` JSON structure on error.
