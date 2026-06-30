from django.conf import settings
from django.db import models

from shared.models import UUIDModel


class VocabularyWord(UUIDModel):
    word = models.CharField(max_length=100, unique=True)
    definition = models.TextField()
    difficulty = models.CharField(max_length=20, blank=True)
    examples = models.JSONField(default=list, blank=True)

    class Meta:
        db_table = "vocabulary_words"
        ordering = ["word"]

    def __str__(self):
        return self.word


class UserVocabulary(UUIDModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="vocabulary_items")
    vocabulary = models.ForeignKey(VocabularyWord, on_delete=models.CASCADE, related_name="user_items")
    mastered = models.BooleanField(default=False)
    times_seen = models.IntegerField(default=0)
    learned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "user_vocabulary"
        unique_together = ("user", "vocabulary")

    def __str__(self):
        return f"{self.user_id}: {self.vocabulary.word}"
