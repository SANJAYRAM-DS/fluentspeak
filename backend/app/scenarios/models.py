import uuid

from django.db import models

from backend.app.topics.models import Topic
from backend.app.users.models import User


class Difficulty(models.TextChoices):
    A1 = "A1", "A1 - Beginner"
    A2 = "A2", "A2 - Elementary"
    B1 = "B1", "B1 - Intermediate"
    B2 = "B2", "B2 - Upper Intermediate"
    C1 = "C1", "C1 - Advanced"
    C2 = "C2", "C2 - Proficient"


class Scenario(models.Model):
    """
    Conversation scenarios.

    Can be:
    - System scenarios
    - User-created scenarios
    - AI-generated scenarios (future)
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="scenarios"
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_scenarios"
    )

    title = models.CharField(
        max_length=200
    )

    description = models.TextField(
        blank=True
    )

    ai_role = models.CharField(
        max_length=100
    )

    user_role = models.CharField(
        max_length=100
    )

    opening_prompt = models.TextField(
        blank=True
    )

    learning_objective = models.TextField(
        blank=True
    )

    difficulty = models.CharField(
        max_length=20,
        choices=Difficulty.choices,
        default=Difficulty.A1
    )

    grammar_focus = models.CharField(
        max_length=100,
        blank=True
    )

    vocabulary_focus = models.TextField(
        blank=True
    )

    max_turns = models.PositiveIntegerField(
        default=10
    )

    is_system = models.BooleanField(
        default=False
    )

    is_public = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "scenarios"
        ordering = ["title"]
        verbose_name = "Scenario"
        verbose_name_plural = "Scenarios"

    def __str__(self):
        return self.title