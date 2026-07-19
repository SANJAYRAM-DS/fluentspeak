# Error Handling Strategy

In a production API, error handling must be consistent. A mobile app developer needs to know exactly what JSON format an error will take.

## 1. Custom Exceptions
Instead of manually crafting `JsonResponse` objects inside our service functions (which is messy), we raise custom Python exceptions defined in `core/exceptions.py`:
- `AuthenticationError` (401)
- `PermissionDeniedError` (403)
- `NotFoundError` (404)
- `ValidationError` (400)
- `ConflictError` (409)

## 2. The Global Exception Handler
In `api.py`, we registered a global handler:
```python
@api.exception_handler(FluentSpeakError)
def fluentspeak_error_handler(request, exc):
    return JsonResponse({"message": exc.message}, status=exc.status_code)
```
Whenever `raise ValidationError("Passwords do not match")` happens deep inside `validators.py`, the execution immediately stops, bubbles up to Django Ninja, is caught by this handler, and is transformed into:
```json
HTTP 400 Bad Request
{
    "message": "Passwords do not match"
}
```

## 3. Database Rollbacks
In the `register` and `change_password` functions, we use `with transaction.atomic():`. 
If an exception is raised *anywhere* inside that block, Django automatically intercepts it and rolls back any database writes that occurred within the block. This prevents half-created users or orphaned profiles.
