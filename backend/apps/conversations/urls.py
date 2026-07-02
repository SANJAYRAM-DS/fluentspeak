from django.urls import path

from .views import (
    ConversationDetailView,
    ConversationListCreateView,
    ConversationMessageListView,
    ConversationSwitchView,
    ConversationTurnDetailView,
    ConversationTurnStreamView,
    ConversationTurnView,
)


urlpatterns = [
    path("", ConversationListCreateView.as_view(), name="conversation-list-create"),
    path("<uuid:pk>", ConversationDetailView.as_view(), name="conversation-detail"),
    path("<uuid:pk>/switch", ConversationSwitchView.as_view(), name="conversation-switch"),
    path("<uuid:pk>/messages", ConversationMessageListView.as_view(), name="conversation-messages"),
    path("<uuid:pk>/turns", ConversationTurnView.as_view(), name="conversation-turn"),
    path("<uuid:pk>/turns/stream", ConversationTurnStreamView.as_view(), name="conversation-turn-stream"),
    path("<uuid:pk>/turns/<uuid:turn_pk>", ConversationTurnDetailView.as_view(), name="conversation-turn-detail"),
]
