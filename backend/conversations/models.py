import uuid

from django.db import models

from users.models import User
from topics.models import Topic
from scenarios.models import Scenario
from vocabulary.models import VocabularyWord


class ConversationStatus(models.TextChoices):
    ACTIVE = "active", "Active"
    COMPLETED = "completed", "Completed"
    ARCHIVED = "archived", "Archived"


class ConversationStage(models.TextChoices):
    INTRODUCTION = "introduction", "Introduction"
    PRACTICE = "practice", "Practice"
    FEEDBACK = "feedback", "Feedback"
    COMPLETED = "completed", "Completed"


class MessageSender(models.TextChoices):
    USER = "user", "User"
    AI = "ai", "AI"


class MessageType(models.TextChoices):
    TEXT = "text", "Text"
    SYSTEM = "system", "System"
    CORRECTION = "correction", "Correction"
    VOCABULARY = "vocabulary", "Vocabulary"


class Conversation(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="conversations"
    )

    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="conversations"
    )

    scenario = models.ForeignKey(
        Scenario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="conversations"
    )

    title = models.CharField(max_length=255)

    status = models.CharField(
        max_length=20,
        choices=ConversationStatus.choices,
        default=ConversationStatus.ACTIVE
    )

    current_turn = models.PositiveIntegerField(default=0)

    total_turns = models.PositiveIntegerField(default=0)

    started_at = models.DateTimeField(auto_now_add=True)

    ended_at = models.DateTimeField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "conversations"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class ConversationState(models.Model):

    conversation = models.OneToOneField(
        Conversation,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="state"
    )

    stage = models.CharField(
        max_length=30,
        choices=ConversationStage.choices,
        default=ConversationStage.INTRODUCTION
    )

    current_goal = models.TextField(blank=True)

    progress_percentage = models.PositiveSmallIntegerField(default=0)

    conversation_summary = models.TextField(blank=True)

    last_vocab = models.ForeignKey(
        VocabularyWord,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="conversation_states"
    )

    prompt_version = models.CharField(
        max_length=20,
        default="v1"
    )

    state_data = models.JSONField(
        default=dict,
        blank=True
    )

    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "conversation_states"

    def __str__(self):
        return f"State - {self.conversation.title}"


class Message(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name="messages"
    )

    sender = models.CharField(
        max_length=20,
        choices=MessageSender.choices
    )

    turn_number = models.PositiveIntegerField()

    message = models.TextField()

    message_type = models.CharField(
        max_length=30,
        choices=MessageType.choices,
        default=MessageType.TEXT
    )

    token_count = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "messages"
        ordering = ["turn_number"]

    def __str__(self):
        return f"{self.sender} - Turn {self.turn_number}"


class MessageFeedback(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    message = models.OneToOneField(
        Message,
        on_delete=models.CASCADE,
        related_name="feedback"
    )

    grammar_correction = models.TextField(blank=True)

    optimized_sentence = models.TextField(blank=True)

    explanation = models.TextField(blank=True)

    next_question = models.TextField(blank=True)

    vocabulary = models.ForeignKey(
        VocabularyWord,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="feedbacks"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "message_feedback"

    def __str__(self):
        return f"Feedback - {self.message.id}"