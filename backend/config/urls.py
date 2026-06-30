from django.urls import include, path
from rest_framework_simplejwt.views import TokenRefreshView

from apps.users.views import LoginView, RegisterView


urlpatterns = [
    path("api/v1/auth/register", RegisterView.as_view(), name="auth-register"),
    path("api/v1/auth/login", LoginView.as_view(), name="auth-login"),
    path("api/v1/auth/refresh", TokenRefreshView.as_view(), name="auth-refresh"),
    path("api/v1/topics", include("apps.topics.urls")),
    path("api/v1/scenarios", include("apps.scenarios.urls")),
    path("api/v1/conversations", include("apps.conversations.urls")),
    path("api/v1/vocabulary", include("apps.vocabulary.urls")),
    path("api/v1/progress", include("apps.users.progress_urls")),
]
