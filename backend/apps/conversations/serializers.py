from rest_framework import serializers

from apps.topics.serializers import TopicSerializer
from apps.scenarios.serializers import ScenarioSerializer
from .models import Conversation, ConversationState, Message, MessageFeedback


class MessageFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageFeedback
        fields = ["id", "correction", "optimized_response", "next_question"]


class MessageSerializer(serializers.ModelSerializer):
    feedback = MessageFeedbackSerializer(read_only=True)

    class Meta:
        model = Message
        fields = [
            "id",
            "conversation",
            "role",
            "content",
            "turn_number",
            "token_count",
            "latency_ms",
            "provider",
            "model",
            "created_at",
            "feedback",
        ]
        read_only_fields = [
            "id",
            "conversation",
            "role",
            "turn_number",
            "token_count",
            "latency_ms",
            "provider",
            "model",
            "created_at",
            "feedback",
        ]


class ConversationStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConversationState
        fields = ["stage", "tone", "goal_progress", "last_vocab_word", "summary"]


class ConversationSerializer(serializers.ModelSerializer):
    topic = TopicSerializer(read_only=True)
    scenario = ScenarioSerializer(read_only=True)
    messages = MessageSerializer(many=True, read_only=True)
    state = ConversationStateSerializer(read_only=True)

    class Meta:
        model = Conversation
        fields = [
            "id",
            "topic",
            "scenario",
            "title",
            "status",
            "current_turn",
            "summary",
            "created_at",
            "updated_at",
            "messages",
            "state",
        ]


class CreateConversationSerializer(serializers.Serializer):
    topic_id = serializers.UUIDField(required=False)
    scenario_id = serializers.UUIDField(required=False)
    title = serializers.CharField(max_length=255, required=False, allow_blank=True)

    def validate(self, attrs):
        if not attrs.get("topic_id") and not attrs.get("scenario_id"):
            raise serializers.ValidationError("Either topic_id or scenario_id is required.")
        return attrs


class SendMessageSerializer(serializers.Serializer):
    message = serializers.CharField()
    client_message_id = serializers.UUIDField(required=False)
    conversation_revision = serializers.IntegerField(required=False)


class TurnResponseSerializer(serializers.Serializer):
    turn_id = serializers.UUIDField()
    conversation_id = serializers.UUIDField()
    reply = serializers.CharField()
    correction = serializers.CharField()
    optimized_response = serializers.CharField()
    vocabulary = serializers.DictField(required=False, allow_null=True)
    next_question = serializers.CharField(required=False, allow_blank=True)
    conversation_revision = serializers.IntegerField()
