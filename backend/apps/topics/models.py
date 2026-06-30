from django.db import models

from shared.models import UUIDModel


class Topic(UUIDModel):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    difficulty = models.CharField(max_length=20, blank=True)
    category = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "topics"
        ordering = ["title"]

    def __str__(self):
        return self.title
