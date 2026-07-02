from django.urls import include, path


urlpatterns = [
    path("", include("apps.web.urls")),
    path("api/v1/auth/", include("apps.users.urls")),
    path("api/v1/topics", include("apps.topics.urls")),
    path("api/v1/scenarios", include("apps.scenarios.urls")),
    path("api/v1/conversations", include("apps.conversations.urls")),
    path("api/v1/vocabulary", include("apps.vocabulary.urls")),
    path("api/v1/progress", include("apps.users.progress_urls")),
    path("api/v1/me/progress", include("apps.users.progress_urls")),
]
