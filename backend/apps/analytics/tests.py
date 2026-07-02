from django.contrib.auth import get_user_model
from django.test import TestCase

from apps.analytics.models import AnalyticsEvent
from apps.tasks.tasks import track_event


class AnalyticsEventTests(TestCase):
    def test_track_event_persists_analytics_event(self):
        user = get_user_model().objects.create_user(email="analytics@example.com", password="password123")
        result = track_event(user.id, "conversation_started", {"topic": "Travel"})
        self.assertEqual(AnalyticsEvent.objects.count(), 1)
        self.assertEqual(result["event_name"], "conversation_started")

