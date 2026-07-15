import uuid

from django.db import models

from users.models import User


class NotificationType(models.TextChoices):
    SYSTEM = "system", "System"
    REMINDER = "reminder", "Reminder"
    ACHIEVEMENT = "achievement", "Achievement"
    LEARNING = "learning", "Learning"


class Notification(models.Model):
    """
    Stores notifications sent to users.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notifications"
    )

    title = models.CharField(
        max_length=255
    )

    message = models.TextField()

    notification_type = models.CharField(
        max_length=30,
        choices=NotificationType.choices,
        default=NotificationType.SYSTEM
    )

    is_read = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        db_table = "notifications"
        ordering = ["-created_at"]
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"

    def __str__(self):
        return f"{self.title} ({self.user.email})"