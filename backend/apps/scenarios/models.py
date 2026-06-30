from django.conf import settings
from django.db import models

from shared.models import UUIDModel


class Scenario(UUIDModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="scenarios")
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    ai_role = models.CharField(max_length=100)
    user_role = models.CharField(max_length=100)
    goal = models.TextField(blank=True)
    max_turns = models.IntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "scenarios"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
