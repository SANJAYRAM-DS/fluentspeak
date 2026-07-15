from django.contrib import admin

from .models import Topic


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "difficulty",
        "is_active",
        "created_at",
    )

    search_fields = (
        "title",
        "category",
    )

    list_filter = (
        "difficulty",
        "category",
        "is_active",
    )

    ordering = (
        "title",
    )