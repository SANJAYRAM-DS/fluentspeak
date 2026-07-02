import json

from django.db import transaction
from rest_framework.exceptions import ValidationError

from apps.ai.services.groq_client import GroqClient
from apps.scenarios.models import Scenario
from apps.topics.models import Topic

from ..models import Conversation, ConversationState, Message, MessageFeedback
from ..repositories import ConversationRepository
from .memory_service import MemoryService
from .prompt_builder import PromptBuilder
from .vocabulary_service import VocabularyService
from .response_validator import ResponseValidator
from .state_machine import ConversationStateMachine


class ConversationService:
    @staticmethod
    def create_conversation(user, *, topic_id=None, scenario_id=None, title=""):
        topic = Topic.objects.filter(id=topic_id).first() if topic_id else None
        scenario = Scenario.objects.filter(id=scenario_id, user=user).first() if scenario_id else None
        if topic_id and topic is None:
            raise ValidationError({"topic_id": "Topic not found."})
        if scenario_id and scenario is None:
            raise ValidationError({"scenario_id": "Scenario not found."})
        conversation = Conversation.objects.create(
            user=user,
            topic=topic,
            scenario=scenario,
            title=title or (scenario.title if scenario else topic.title),
        )
        ConversationState.objects.create(conversation=conversation)
        first_message = "Hello. Let's practice together."
        Message.objects.create(
            conversation=conversation,
            role=Message.ROLE_ASSISTANT,
            content=first_message,
            turn_number=0,
        )
        return {"conversation": conversation, "first_message": first_message}

    @staticmethod
    def generate_turn(user, conversation_id, message, client_message_id=None, conversation_revision=None):
        conversation = ConversationRepository.get_for_user(user, conversation_id)
        if conversation_revision is not None and conversation_revision != conversation.current_turn:
            raise ValidationError({"conversation_revision": "Conversation revision mismatch."})
        learned_words = VocabularyService.get_seen_words(user)
        prompt = PromptBuilder.build(conversation, message, learned_words)
        ai_client = GroqClient()
        ai_result = ai_client.complete_json(prompt)
        ai_response = ResponseValidator.validate(json.loads(ai_result.content))
        turn_number = conversation.current_turn + 1
        with transaction.atomic():
            Message.objects.create(
                conversation=conversation,
                role=Message.ROLE_USER,
                content=message,
                turn_number=turn_number,
                provider="user",
            )
            assistant_message = Message.objects.create(
                conversation=conversation,
                role=Message.ROLE_ASSISTANT,
                content=ai_response["reply"],
                turn_number=turn_number,
                token_count=ai_result.token_count,
                latency_ms=ai_result.latency_ms,
                provider=ai_result.provider,
                model=ai_result.model,
            )
            MessageFeedback.objects.create(
                message=assistant_message,
                correction=ai_response["correction"],
                optimized_response=ai_response["optimized_response"],
                next_question=ai_response.get("next_question", ""),
            )
            vocabulary_payload = VocabularyService.register_word(user, ai_response.get("vocabulary"))
            MemoryService.update_summary(conversation, user_message=message, assistant_reply=ai_response["reply"])
            conversation.current_turn = turn_number
            conversation.save(update_fields=["current_turn", "summary", "updated_at"])
            state, _ = ConversationState.objects.get_or_create(conversation=conversation)
            ConversationStateMachine.advance(state)
        return {
            "turn_id": assistant_message.id,
            "conversation_id": conversation.id,
            "reply": ai_response["reply"],
            "correction": ai_response["correction"],
            "optimized_response": ai_response["optimized_response"],
            "vocabulary": vocabulary_payload,
            "next_question": ai_response.get("next_question", ""),
            "conversation_revision": conversation.current_turn,
        }

    @staticmethod
    def stream_turn(user, conversation_id, message):
        result = ConversationService.generate_turn(user, conversation_id, message)
        payload = json.dumps(result)
        for start in range(0, len(payload), 32):
            yield f"data: {payload[start:start + 32]}\n\n"
        yield "event: done\ndata: {}\n\n"
