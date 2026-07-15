import uuid

from django.db import models


class Difficulty(models.TextChoices):
    BEGINNER = "beginner", "Beginner"
    INTERMEDIATE = "intermediate", "Intermediate"
    ADVANCED = "advanced", "Advanced"


class Topic(models.Model):
    """
    Conversation topics available in FluentSpeak.
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

    description = models.TextField(
        blank=True
    )

    category = models.CharField(
        max_length=50
    )

    difficulty = models.CharField(
        max_length=20,
        choices=Difficulty.choices,
        default=Difficulty.BEGINNER
    )

    image_url = models.TextField(
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        db_table = "topics"
        ordering = ["title"]
        verbose_name = "Topic"
        verbose_name_plural = "Topics"

    def __str__(self):
        return self.title