"""
Custom Exceptions for the FluentSpeak API.

These exceptions allow us to raise errors deep in our services
and catch them at the API layer (in api.py) to return consistent
HTTP responses.
"""

class FluentSpeakError(Exception):
    """Base exception for all custom API errors."""
    
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class AuthenticationError(FluentSpeakError):
    """Raised when authentication fails (wrong password, invalid token)."""
    
    def __init__(self, message: str = "Invalid credentials"):
        super().__init__(message, status_code=401)


class PermissionDeniedError(FluentSpeakError):
    """Raised when an authenticated user lacks required privileges."""
    
    def __init__(self, message: str = "Permission denied"):
        super().__init__(message, status_code=403)


class NotFoundError(FluentSpeakError):
    """Raised when a requested resource does not exist."""
    
    def __init__(self, message: str = "Resource not found"):
        super().__init__(message, status_code=404)


class ValidationError(FluentSpeakError):
    """Raised for business logic validation failures (e.g., duplicate email)."""
    
    def __init__(self, message: str = "Validation failed"):
        super().__init__(message, status_code=400)


class ConflictError(FluentSpeakError):
    """Raised for resource conflicts (e.g., trying to register an existing email)."""
    
    def __init__(self, message: str = "Resource conflict"):
        super().__init__(message, status_code=409)
