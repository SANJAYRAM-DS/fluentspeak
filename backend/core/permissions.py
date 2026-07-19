"""
Django Ninja Authentication Middleware.

This defines the `AuthBearer` class, which protects API routes.
When applied to a route, it intercepts the request, extracts the JWT,
validates it, and attaches the user object to `request.auth`.
"""
from typing import Optional, Any
from django.http import HttpRequest
from ninja.security import HttpBearer

from backend.app.users.models import User
from backend.core.jwt import decode_token
from backend.core.exceptions import AuthenticationError
from backend.api.auth.repository import create_audit_log
from backend.core.utils import get_client_ip, get_user_agent


class AuthBearer(HttpBearer):
    """
    Extracts the Bearer token from the Authorization header,
    decodes it, and retrieves the corresponding User.
    """
    
    def authenticate(self, request: HttpRequest, token: str) -> Optional[Any]:
        try:
            # 1. Decode and validate the JWT signature and expiration
            # We specifically expect an "access" token here.
            payload = decode_token(token, token_type="access")
            
            # 2. Extract the user ID (subject)
            user_id = payload.get("sub")
            if not user_id:
                raise AuthenticationError("Token missing subject claim.")
                
            # 3. Fetch the user from the database
            user = User.objects.filter(id=user_id).first()
            
            if not user:
                raise AuthenticationError("User not found.")
                
            if not user.is_active:
                raise AuthenticationError("User account is disabled.")
                
            # 4. Success! Return the user object.
            # Django Ninja automatically attaches this to `request.auth`.
            return user
            
        except AuthenticationError as e:
            # Log the failure before re-raising
            reason = str(e)
            action = "INVALID_TOKEN"
            
            if "disabled" in reason.lower():
                action = "ACCOUNT_DISABLED"
            elif "not found" in reason.lower():
                action = "UNAUTHORIZED_ACCESS"
                
            create_audit_log(
                user=None,
                action=action,
                ip_address=get_client_ip(request),
                user_agent=get_user_agent(request),
                metadata={"reason": reason}
            )
            # Re-raise custom auth errors so the global exception handler
            # can catch them and return a clean 401 JSON response.
            raise e
        except Exception as e:
            create_audit_log(
                user=None,
                action="UNAUTHORIZED_ACCESS",
                ip_address=get_client_ip(request),
                user_agent=get_user_agent(request),
                metadata={"reason": "Unexpected error"}
            )
            # Catch unexpected errors to prevent 500 crashes
            raise AuthenticationError("Authentication failed.")
