from django.contrib import admin

from .models import Topic


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "difficulty",
        "grammar_focus",
        "estimated_turns",
        "display_order",
        "is_active",
    )

    list_filter = (
        "category",
        "difficulty",
        "is_active",
    )

    search_fields = (
        "title",
        "description",
        "grammar_focus",
        "vocabulary_focus",
    )

    ordering = (
        "display_order",
        "title",
    )