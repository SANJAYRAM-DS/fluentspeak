from ninja import NinjaAPI
from django.http import JsonResponse
from backend.api.auth.router import router as auth_router
from backend.api.topics.router import router as topics_router
from backend.core.exceptions import FluentSpeakError

api = NinjaAPI(
    title = "FluentSpeak API",
    version = "1.0.0",
    urls_namespace='api',
)

@api.exception_handler(FluentSpeakError)
def fluentspeak_error_handler(request, exc):
    """
    Catches any custom FluentSpeakError (like AuthenticationError, ValidationError)
    raised anywhere in the service layer and returns a clean JSON response.
    """
    return JsonResponse(
        {"message": exc.message}, 
        status=exc.status_code
    )

api.add_router("/auth/", auth_router)
api.add_router("/topics", topics_router)