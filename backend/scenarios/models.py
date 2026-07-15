import uuid

from django.db import models
from users.models import User
from topics.models import Topic


class Difficulty(models.TextChoices):
    BEGINNER = "beginner", "Beginner"
    INTERMEDIATE = "intermediate", "Intermediate"
    ADVANCED = "advanced", "Advanced"


class Scenario(models.Model):
    """
    User-created conversation scenarios.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="scenarios"
    )

    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="scenarios"
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

    objective = models.TextField(
        blank=True
    )

    difficulty = models.CharField(
        max_length=20,
        choices=Difficulty.choices,
        default=Difficulty.BEGINNER
    )

    max_turns = models.PositiveIntegerField(
        default=10
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
        ordering = ["-created_at"]
        verbose_name = "Scenario"
        verbose_name_plural = "Scenarios"

    def __str__(self):
        return self.title