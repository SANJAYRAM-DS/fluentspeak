from django.conf import settings
from django.db import models

from shared.models import UUIDModel


class AuditLog(UUIDModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="audit_logs")
    action = models.CharField(max_length=100)
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "audit_logs"
        ordering = ["-created_at"]

    def __str__(self):
        return self.action


class AnalyticsEvent(UUIDModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="analytics_events")
    event_name = models.CharField(max_length=100)
    payload = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "analytics_events"
        ordering = ["-created_at"]

    def __str__(self):
        return self.event_name
