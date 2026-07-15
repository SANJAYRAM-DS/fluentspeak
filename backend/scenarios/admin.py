from django.contrib import admin

from .models import Scenario


@admin.register(Scenario)
class ScenarioAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "user",
        "topic",
        "difficulty",
        "max_turns",
        "is_public",
        "created_at",
    )

    search_fields = (
        "title",
        "user__email",
        "topic__title",
    )

    list_filter = (
        "difficulty",
        "is_public",
        "topic",
    )

    ordering = (
        "-created_at",
    )