from django.contrib import admin

from .models import UserProgress, AuditLog


@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "total_conversations",
        "total_messages",
        "vocabulary_learned",
        "current_streak",
        "updated_at",
    )

    search_fields = (
        "user__email",
    )

    ordering = (
        "-updated_at",
    )


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):

    list_display = (
        "action",
        "user",
        "entity_type",
        "ip_address",
        "created_at",
    )

    list_filter = (
        "action",
        "entity_type",
    )

    search_fields = (
        "action",
        "user__email",
    )

    ordering = (
        "-created_at",
    )