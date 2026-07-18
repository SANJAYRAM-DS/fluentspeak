import uuid

from django.db import models


class Difficulty(models.TextChoices):
    A1 = "A1", "A1 - Beginner"
    A2 = "A2", "A2 - Elementary"
    B1 = "B1", "B1 - Intermediate"
    B2 = "B2", "B2 - Upper Intermediate"
    C1 = "C1", "C1 - Advanced"
    C2 = "C2", "C2 - Proficient"


class Topic(models.Model):
    """
    Conversation topics available for users.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    title = models.CharField(
        max_length=100,
        unique=True
    )

    description = models.TextField()

    category = models.CharField(
        max_length=50
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

    estimated_turns = models.PositiveIntegerField(
        default=10
    )

    image_url = models.TextField(
        blank=True
    )

    icon = models.CharField(
        max_length=50,
        blank=True
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        db_table = "topics"
        ordering = ["display_order", "title"]
        verbose_name = "Topic"
        verbose_name_plural = "Topics"

    def __str__(self):
        return self.title