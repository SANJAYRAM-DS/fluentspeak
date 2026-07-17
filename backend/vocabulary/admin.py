from django.contrib import admin

from .models import VocabularyWord, UserVocabulary


@admin.register(VocabularyWord)
class VocabularyWordAdmin(admin.ModelAdmin):

    list_display = (
        "word",
        "topic",
        "part_of_speech",
        "difficulty",
        "created_at",
    )

    list_filter = (
        "topic",
        "difficulty",
        "part_of_speech",
    )

    search_fields = (
        "word",
        "definition",
    )

    ordering = (
        "word",
    )


@admin.register(UserVocabulary)
class UserVocabularyAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "vocabulary",
        "mastery_level",
        "mastered",
        "times_seen",
        "times_practiced",
    )

    list_filter = (
        "mastered",
    )

    search_fields = (
        "user__email",
        "vocabulary__word",
    )