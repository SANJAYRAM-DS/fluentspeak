from django.urls import path

from .views import AuthView, ChatView, DashboardView, ProgressView, VocabularyView


urlpatterns = [
    path("", AuthView.as_view(), name="home"),
    path("auth/", AuthView.as_view(), name="auth"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("chat/", ChatView.as_view(), name="chat"),
    path("vocabulary/", VocabularyView.as_view(), name="vocabulary"),
    path("progress/", ProgressView.as_view(), name="progress"),
]
