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
        "provider_name",
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
        "total_tokens",
        "latency_ms",
        "request_status",
        "created_at",
    )

    list_filter = (
        "request_status",
        "provider",
    )

    search_fields = (
        "conversation__title",
    )

    ordering = (
        "-created_at",
    )