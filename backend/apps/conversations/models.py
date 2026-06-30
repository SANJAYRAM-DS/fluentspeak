from django.conf import settings
from django.db import models

from shared.models import TimestampedModel, UUIDModel


class Conversation(TimestampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="conversations")
    topic = models.ForeignKey("topics.Topic", on_delete=models.SET_NULL, null=True, blank=True, related_name="conversations")
    scenario = models.ForeignKey("scenarios.Scenario", on_delete=models.SET_NULL, null=True, blank=True, related_name="conversations")
    title = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=20, default="active")
    current_turn = models.IntegerField(default=0)
    summary = models.TextField(blank=True)

    class Meta:
        db_table = "conversations"
        ordering = ["-updated_at"]

    def __str__(self):
        return self.title or str(self.id)


class Message(UUIDModel):
    ROLE_USER = "user"
    ROLE_ASSISTANT = "assistant"
    ROLE_SYSTEM = "system"

    ROLE_CHOICES = (
        (ROLE_USER, "User"),
        (ROLE_ASSISTANT, "Assistant"),
        (ROLE_SYSTEM, "System"),
    )

    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="messages")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    content = models.TextField()
    turn_number = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "messages"
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.role}: {self.content[:40]}"


class MessageFeedback(UUIDModel):
    message = models.OneToOneField(Message, on_delete=models.CASCADE, related_name="feedback")
    correction = models.TextField(blank=True)
    optimized_response = models.TextField(blank=True)
    next_question = models.TextField(blank=True)

    class Meta:
        db_table = "message_feedback"


class ConversationState(models.Model):
    conversation = models.OneToOneField(
        Conversation,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="state",
    )
    stage = models.CharField(max_length=30, default="opening")
    tone = models.CharField(max_length=30, default="friendly")
    goal_progress = models.IntegerField(default=0)
    last_vocab_word = models.CharField(max_length=100, blank=True)
    summary = models.TextField(blank=True)

    class Meta:
        db_table = "conversation_states"

    def __str__(self):
        return f"{self.conversation_id}: {self.stage}"
