from django.contrib import admin

from .models import AIProvider, AIRequest


@admin.register(AIProvider)
class AIProviderAdmin(admin.ModelAdmin):

    list_display = (
        "provider_name",
        "model_name",
        "priority",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "provider_name",
        "model_name",
    )

    ordering = (
        "priority",
    )


@admin.register(AIRequest)
class AIRequestAdmin(admin.ModelAdmin):

    list_display = (
        "conversation",
        "provider",
        "model_name",
        "request_status",
        "total_tokens",
        "latency_ms",
        "created_at",
    )

    list_filter = (
        "provider",
        "request_status",
    )

    search_fields = (
        "conversation__title",
        "provider__provider_name",
        "model_name",
    )

    ordering = (
        "-created_at",
    )