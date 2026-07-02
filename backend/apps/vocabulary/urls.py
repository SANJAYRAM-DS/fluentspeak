from django.urls import path

from .views import LearnedWordsView, MarkMasteredView, VocabularyStatsView


urlpatterns = [
    path("", LearnedWordsView.as_view(), name="vocabulary-root"),
    path("learned", LearnedWordsView.as_view(), name="learned-words"),
    path("learned/<uuid:pk>", MarkMasteredView.as_view(), name="learned-word-delete"),
    path("learned/<uuid:pk>/master", MarkMasteredView.as_view(), name="mark-mastered"),
    path("stats", VocabularyStatsView.as_view(), name="vocabulary-stats"),
]
