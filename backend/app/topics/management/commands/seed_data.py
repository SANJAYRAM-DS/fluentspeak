from django.core.management.base import BaseCommand

from backend.app.content.travel import TRAVEL
from backend.app.content.food import FOOD
from backend.app.content.shopping import SHOPPING
from backend.app.content.interview import INTERVIEW
from backend.app.content.daily import DAILY

from backend.app.topics.models import Topic
from backend.app.scenarios.models import Scenario
from backend.app.vocabulary.models import VocabularyWord

CONTENT = [
    TRAVEL,
    FOOD,
    SHOPPING,
    INTERVIEW,
    DAILY,
]

class Command(BaseCommand):
    help = "Seed initial application data"

    def handle(self, *args, **kwargs):

        self.stdout.write(self.style.SUCCESS("Starting database seeding...\n"))

        for content in CONTENT:
            self.seed_topic(content)

        self.stdout.write(self.style.SUCCESS("\nDatabase seeded successfully."))
    
    def seed_topic(self, content):

        topic_data = content["topic"]

        topic, created = Topic.objects.get_or_create(
            title=topic_data["title"],
            defaults=topic_data,
        )

        if created:
            self.stdout.write(
                self.style.SUCCESS(f"Created Topic: {topic.title}")
            )
        else:
            self.stdout.write(
                self.style.WARNING(f"Topic already exists: {topic.title}")
            )

        self.seed_scenarios(topic, content)

        self.seed_vocabulary(topic, content)
    
    def seed_scenarios(self, topic, content):

        for scenario in content["scenarios"]:

            Scenario.objects.get_or_create(
                topic=topic,
                title=scenario["title"],
                defaults={
                    **scenario,
                    "topic": topic,
                },
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"   Added {len(content['scenarios'])} scenarios."
            )
        )
    
    def seed_vocabulary(self, topic, content):

        for word in content["vocabulary"]:

            VocabularyWord.objects.get_or_create(
                word=word["word"],
                topic=topic,
                defaults={
                    "definition": word["definition"],
                    "pronunciation": word.get("pronunciation", ""),
                    "part_of_speech": word.get("part_of_speech", ""),
                    "difficulty": word.get("difficulty", "A1"),
                    "example_sentences": word.get("example_sentences", []),
                },
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"   Added {len(content['vocabulary'])} vocabulary words."
            )
        )