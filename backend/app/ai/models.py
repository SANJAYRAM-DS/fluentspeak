import uuid

from django.db import models

from backend.app.conversations.models import Conversation


class RequestStatus(models.TextChoices):
    SUCCESS = "success", "Success"
    FAILED = "failed", "Failed"
    TIMEOUT = "timeout", "Timeout"


class AIProvider(models.Model):
    """
    Stores AI provider configurations.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    provider_name = models.CharField(
        max_length=50,
        unique=True
    )

    model_name = models.CharField(
        max_length=100
    )

    api_version = models.CharField(
        max_length=50,
        blank=True
    )

    priority = models.PositiveIntegerField(
        default=1
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        db_table = "ai_providers"
        ordering = ["priority"]
        verbose_name = "AI Provider"
        verbose_name_plural = "AI Providers"

    def __str__(self):
        return f"{self.provider_name} ({self.model_name})"


class AIRequest(models.Model):
    """
    Logs every LLM request made by the application.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name="ai_requests"
    )

    provider = models.ForeignKey(
        AIProvider,
        on_delete=models.CASCADE,
        related_name="requests"
    )

    # Actual model used for this request
    model_name = models.CharField(
        max_length=100
    )

    prompt_tokens = models.PositiveIntegerField(
        default=0
    )

    completion_tokens = models.PositiveIntegerField(
        default=0
    )

    total_tokens = models.PositiveIntegerField(
        default=0
    )

    latency_ms = models.PositiveIntegerField(
        default=0
    )

    request_status = models.CharField(
        max_length=20,
        choices=RequestStatus.choices,
        default=RequestStatus.SUCCESS
    )

    error_message = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        db_table = "ai_requests"
        ordering = ["-created_at"]
        verbose_name = "AI Request"
        verbose_name_plural = "AI Requests"

    def __str__(self):
        return (
            f"{self.provider.provider_name} - "
            f"{self.model_name} - "
            f"{self.request_status}"
        )