from django.core.management import call_command
from django.test import TestCase

from apps.topics.models import Topic


class TopicSeedTests(TestCase):
    def test_seed_topics_creates_default_list(self):
        call_command("seed_topics", verbosity=0)
        self.assertGreaterEqual(Topic.objects.count(), 50)

