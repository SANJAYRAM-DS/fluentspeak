from django.urls import path

from .views import TopicDetailView, TopicListView


urlpatterns = [
    path("", TopicListView.as_view(), name="topic-list"),
    path("<uuid:pk>", TopicDetailView.as_view(), name="topic-detail"),
]
