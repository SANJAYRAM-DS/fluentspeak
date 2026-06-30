from django.db import models

from shared.models import UUIDModel


class AIProvider(UUIDModel):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    priority = models.IntegerField(default=100)
    status = models.CharField(max_length=20, default="active")

    class Meta:
        db_table = "ai_providers"
        ordering = ["priority", "name"]

    def __str__(self):
        return f"{self.name}:{self.model}"
