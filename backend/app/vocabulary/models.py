import uuid

from django.db import models

from backend.app.users.models import User
from backend.app.topics.models import Topic


class Difficulty(models.TextChoices):
    A1 = "A1", "A1 - Beginner"
    A2 = "A2", "A2 - Elementary"
    B1 = "B1", "B1 - Intermediate"
    B2 = "B2", "B2 - Upper Intermediate"
    C1 = "C1", "C1 - Advanced"
    C2 = "C2", "C2 - Proficient"


class PartOfSpeech(models.TextChoices):
    NOUN = "noun", "Noun"
    VERB = "verb", "Verb"
    ADJECTIVE = "adjective", "Adjective"
    ADVERB = "adverb", "Adverb"
    PRONOUN = "pronoun", "Pronoun"
    PREPOSITION = "preposition", "Preposition"
    CONJUNCTION = "conjunction", "Conjunction"
    INTERJECTION = "interjection", "Interjection"


class VocabularyWord(models.Model):
    """
    Master vocabulary dictionary.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    word = models.CharField(
        max_length=100,
    )

    definition = models.TextField()

    pronunciation = models.CharField(
        max_length=255,
        blank=True
    )

    part_of_speech = models.CharField(
        max_length=50,
        choices=PartOfSpeech.choices
    )

    difficulty = models.CharField(
        max_length=20,
        choices=Difficulty.choices,
        default=Difficulty.A1
    )

    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="vocabulary_words"
    )

    example_sentences = models.JSONField(
        default=list,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        db_table = "vocabulary_words"
        ordering = ["word"]
        verbose_name = "Vocabulary Word"
        verbose_name_plural = "Vocabulary Words"

        unique_together = ("word", "topic")

    def __str__(self):
        return self.word


class UserVocabulary(models.Model):
    """
    Tracks a user's progress for each vocabulary word.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="vocabulary"
    )

    vocabulary = models.ForeignKey(
        VocabularyWord,
        on_delete=models.CASCADE,
        related_name="users"
    )

    times_seen = models.PositiveIntegerField(default=0)

    times_practiced = models.PositiveIntegerField(default=0)

    mastery_level = models.PositiveSmallIntegerField(default=0)

    mastered = models.BooleanField(default=False)

    first_seen = models.DateTimeField(auto_now_add=True)

    last_reviewed = models.DateTimeField(
        null=True,
        blank=True
    )

    class Meta:
        db_table = "user_vocabulary"
        unique_together = ("user", "vocabulary")
        verbose_name = "User Vocabulary"
        verbose_name_plural = "User Vocabulary"

    def __str__(self):
        return f"{self.user.email} - {self.vocabulary.word}"