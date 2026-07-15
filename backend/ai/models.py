import uuid

from django.db import models

from conversations.models import Conversation


class ProviderName(models.TextChoices):
    GROQ = "groq", "Groq"
    OPENAI = "openai", "OpenAI"
    GEMINI = "gemini", "Gemini"
    ANTHROPIC = "anthropic", "Anthropic"


class RequestStatus(models.TextChoices):
    SUCCESS = "success", "Success"
    FAILED = "failed", "Failed"
    TIMEOUT = "timeout", "Timeout"


class AIProvider(models.Model):
    """
    Stores available LLM providers.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    provider_name = models.CharField(
        max_length=50,
        choices=ProviderName.choices
    )

    model_name = models.CharField(
        max_length=100
    )

    api_version = models.CharField(
        max_length=50,
        blank=True
    )

    priority = models.PositiveSmallIntegerField(
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
        ordering = ["priority", "provider_name"]
        verbose_name = "AI Provider"
        verbose_name_plural = "AI Providers"

    def __str__(self):
        return f"{self.provider_name} ({self.model_name})"


class AIRequest(models.Model):
    """
    Stores every LLM request made by the application.
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
        on_delete=models.PROTECT,
        related_name="requests"
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
        return f"{self.provider.provider_name} - {self.request_status}"