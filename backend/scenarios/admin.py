from django.contrib import admin

from .models import Scenario


@admin.register(Scenario)
class ScenarioAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "topic",
        "created_by",
        "difficulty",
        "is_system",
        "is_public",
        "max_turns",
        "created_at",
    )

    list_filter = (
        "difficulty",
        "is_system",
        "is_public",
        "topic",
    )

    search_fields = (
        "title",
        "description",
        "learning_objective",
        "grammar_focus",
    )

    ordering = (
        "title",
    )