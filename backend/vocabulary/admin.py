from django.contrib import admin

from .models import VocabularyWord, UserVocabulary


@admin.register(VocabularyWord)
class VocabularyWordAdmin(admin.ModelAdmin):

    list_display = (
        "word",
        "part_of_speech",
        "difficulty",
        "created_at",
    )

    search_fields = (
        "word",
        "definition",
    )

    list_filter = (
        "difficulty",
        "part_of_speech",
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
        "times_seen",
        "times_practiced",
        "mastered",
        "last_reviewed",
    )

    search_fields = (
        "user__email",
        "vocabulary__word",
    )

    list_filter = (
        "mastered",
        "mastery_level",
    )

    ordering = (
        "-last_reviewed",
    )