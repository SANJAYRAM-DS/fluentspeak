from rest_framework.exceptions import ValidationError

from apps.scenarios.models import Scenario
from apps.topics.models import Topic

from ..models import Conversation, ConversationState, Message, MessageFeedback
from ..repositories import ConversationRepository
from .ai_router import AIRouter
from .memory_service import MemoryService
from .prompt_builder import PromptBuilder
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
    def send_message(user, conversation_id, message):
        conversation = ConversationRepository.get_for_user(user, conversation_id)
        turn_number = conversation.current_turn + 1
        Message.objects.create(
            conversation=conversation,
            role=Message.ROLE_USER,
            content=message,
            turn_number=turn_number,
        )
        MemoryService.update_summary(conversation)
        prompt = PromptBuilder.build(conversation, message)
        ai_response = ResponseValidator.validate(AIRouter.generate_reply(prompt))
        assistant_message = Message.objects.create(
            conversation=conversation,
            role=Message.ROLE_ASSISTANT,
            content=ai_response["reply"],
            turn_number=turn_number,
        )
        MessageFeedback.objects.create(
            message=assistant_message,
            correction=ai_response["correction"],
            optimized_response=ai_response["optimized"],
            next_question=ai_response["next_question"],
        )
        conversation.current_turn = turn_number
        conversation.save(update_fields=["current_turn", "updated_at"])
        ConversationStateMachine.advance(conversation.state)
        return {
            "reply": ai_response["reply"],
            "correction": ai_response["correction"],
            "optimized": ai_response["optimized"],
            "vocabulary": ai_response["vocabulary"],
            "examples": ai_response["examples"],
        }
