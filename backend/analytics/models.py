import uuid

from django.db import models

from users.models import User


class UserProgress(models.Model):
    """
    Stores overall learning statistics for each user.
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="progress"
    )

    total_conversations = models.PositiveIntegerField(
        default=0
    )

    total_messages = models.PositiveIntegerField(
        default=0
    )

    vocabulary_learned = models.PositiveIntegerField(
        default=0
    )

    grammar_improvements = models.PositiveIntegerField(
        default=0
    )

    current_streak = models.PositiveIntegerField(
        default=0
    )

    longest_streak = models.PositiveIntegerField(
        default=0
    )

    total_learning_minutes = models.PositiveIntegerField(
        default=0
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "user_progress"
        verbose_name = "User Progress"
        verbose_name_plural = "User Progress"

    def __str__(self):
        return f"{self.user.email} Progress"


class AuditLog(models.Model):
    """
    Stores important system events for auditing.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="audit_logs"
    )

    action = models.CharField(
        max_length=100
    )

    entity_type = models.CharField(
        max_length=50
    )

    entity_id = models.UUIDField(
        null=True,
        blank=True
    )

    ip_address = models.GenericIPAddressField(
        null=True,
        blank=True
    )

    user_agent = models.TextField(
        blank=True
    )

    metadata = models.JSONField(
        default=dict,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        db_table = "audit_logs"
        ordering = ["-created_at"]
        verbose_name = "Audit Log"
        verbose_name_plural = "Audit Logs"

    def __str__(self):
        return f"{self.action} - {self.created_at}"