from django.contrib import admin

from .models import (
    Conversation,
    ConversationState,
    Message,
    MessageFeedback,
)


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "user",
        "topic",
        "status",
        "total_turns",
        "created_at",
    )

    list_filter = (
        "status",
        "topic",
    )

    search_fields = (
        "title",
        "user__email",
    )


@admin.register(ConversationState)
class ConversationStateAdmin(admin.ModelAdmin):

    list_display = (
        "conversation",
        "stage",
        "progress_percentage",
        "last_updated",
    )

    list_filter = (
        "stage",
    )


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):

    list_display = (
        "conversation",
        "sender",
        "turn_number",
        "token_count",
        "created_at",
    )

    list_filter = (
        "sender",
    )

    search_fields = (
        "message",
    )


@admin.register(MessageFeedback)
class MessageFeedbackAdmin(admin.ModelAdmin):

    list_display = (
        "message",
        "vocabulary",
        "created_at",
    )

    search_fields = (
        "grammar_correction",
        "optimized_sentence",
    )