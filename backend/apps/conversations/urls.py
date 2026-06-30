from django.urls import path

from .views import ConversationDetailView, ConversationListCreateView, SendMessageView


urlpatterns = [
    path("", ConversationListCreateView.as_view(), name="conversation-list-create"),
    path("<uuid:pk>", ConversationDetailView.as_view(), name="conversation-detail"),
    path("<uuid:pk>/messages", SendMessageView.as_view(), name="conversation-send-message"),
]
