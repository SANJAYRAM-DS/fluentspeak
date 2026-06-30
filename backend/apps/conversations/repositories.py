from django.shortcuts import get_object_or_404

from .models import Conversation


class ConversationRepository:
    @staticmethod
    def get_for_user(user, conversation_id):
        return get_object_or_404(Conversation, id=conversation_id, user=user)
