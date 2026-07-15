import uuid

from django.db import models
from users.models import User


class Difficulty(models.TextChoices):
    BEGINNER = "beginner", "Beginner"
    INTERMEDIATE = "intermediate", "Intermediate"
    ADVANCED = "advanced", "Advanced"


class PartOfSpeech(models.TextChoices):
    NOUN = "noun", "Noun"
    VERB = "verb", "Verb"
    ADJECTIVE = "adjective", "Adjective"
    ADVERB = "adverb", "Adverb"
    PRONOUN = "pronoun", "Pronoun"
    PREPOSITION = "preposition", "Preposition"
    CONJUNCTION = "conjunction", "Conjunction"
    INTERJECTION = "interjection", "Interjection"
    PHRASE = "phrase", "Phrase"
    OTHER = "other", "Other"


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
        unique=True
    )

    definition = models.TextField()

    pronunciation = models.CharField(
        max_length=255,
        blank=True
    )

    part_of_speech = models.CharField(
        max_length=50,
        choices=PartOfSpeech.choices,
        default=PartOfSpeech.OTHER
    )

    difficulty = models.CharField(
        max_length=20,
        choices=Difficulty.choices,
        default=Difficulty.BEGINNER
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

    def __str__(self):
        return self.word


class UserVocabulary(models.Model):
    """
    Tracks each user's learning progress for vocabulary.
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
        related_name="learners"
    )

    times_seen = models.PositiveIntegerField(
        default=0
    )

    times_practiced = models.PositiveIntegerField(
        default=0
    )

    mastery_level = models.PositiveSmallIntegerField(
        default=0
    )

    mastered = models.BooleanField(
        default=False
    )

    first_seen = models.DateTimeField(
        auto_now_add=True
    )

    last_reviewed = models.DateTimeField(
        null=True,
        blank=True
    )

    class Meta:
        db_table = "user_vocabulary"
        ordering = ["-last_reviewed", "-first_seen"]
        verbose_name = "User Vocabulary"
        verbose_name_plural = "User Vocabulary"

        constraints = [
            models.UniqueConstraint(
                fields=["user", "vocabulary"],
                name="unique_user_vocabulary"
            )
        ]

    def __str__(self):
        return f"{self.user.email} - {self.vocabulary.word}"