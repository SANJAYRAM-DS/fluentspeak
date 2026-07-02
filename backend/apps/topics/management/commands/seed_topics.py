from django.core.management.base import BaseCommand

from apps.topics.models import Topic


TOPICS = [
    {"title": "Travel", "description": "Airport, hotels, transportation, and trips.", "difficulty": "beginner", "category": "lifestyle"},
    {"title": "Technology", "description": "Devices, software, and digital life.", "difficulty": "intermediate", "category": "work"},
    {"title": "Movies", "description": "Films, actors, and reviews.", "difficulty": "beginner", "category": "entertainment"},
    {"title": "Business", "description": "Meetings, planning, and company life.", "difficulty": "advanced", "category": "work"},
    {"title": "Health", "description": "Fitness, nutrition, and wellbeing.", "difficulty": "beginner", "category": "lifestyle"},
    {"title": "Sports", "description": "Games, teams, and competition.", "difficulty": "beginner", "category": "entertainment"},
    {"title": "Food", "description": "Cooking, restaurants, and taste.", "difficulty": "beginner", "category": "lifestyle"},
    {"title": "Education", "description": "Learning, classes, and study habits.", "difficulty": "beginner", "category": "work"},
    {"title": "Career", "description": "Jobs, interviews, and growth.", "difficulty": "intermediate", "category": "work"},
    {"title": "Friendship", "description": "Relationships, trust, and social life.", "difficulty": "beginner", "category": "social"},
    {"title": "Family", "description": "Home life, relatives, and routines.", "difficulty": "beginner", "category": "social"},
    {"title": "Hobbies", "description": "Free time and personal interests.", "difficulty": "beginner", "category": "lifestyle"},
    {"title": "Music", "description": "Songs, artists, and concerts.", "difficulty": "beginner", "category": "entertainment"},
    {"title": "Books", "description": "Reading, genres, and recommendations.", "difficulty": "beginner", "category": "entertainment"},
    {"title": "Weather", "description": "Seasons, forecasts, and climate.", "difficulty": "beginner", "category": "daily life"},
    {"title": "Shopping", "description": "Buying, comparing, and spending.", "difficulty": "beginner", "category": "daily life"},
    {"title": "Finance", "description": "Saving, budgeting, and money habits.", "difficulty": "intermediate", "category": "work"},
    {"title": "Marketing", "description": "Brands, campaigns, and customers.", "difficulty": "advanced", "category": "work"},
    {"title": "Sales", "description": "Pitches, leads, and closing deals.", "difficulty": "advanced", "category": "work"},
    {"title": "Customer Support", "description": "Helping users and solving problems.", "difficulty": "intermediate", "category": "work"},
    {"title": "Coffee Shop", "description": "Ordering drinks and casual chat.", "difficulty": "beginner", "category": "scenario"},
    {"title": "Airport", "description": "Check-in, security, and boarding.", "difficulty": "intermediate", "category": "scenario"},
    {"title": "Hotel Check-In", "description": "Reservations, service, and stay details.", "difficulty": "intermediate", "category": "scenario"},
    {"title": "Job Interview", "description": "Interview questions and answers.", "difficulty": "advanced", "category": "scenario"},
    {"title": "Doctor Visit", "description": "Symptoms, advice, and appointments.", "difficulty": "intermediate", "category": "scenario"},
    {"title": "Dating", "description": "Meetups, interests, and first impressions.", "difficulty": "intermediate", "category": "social"},
    {"title": "College Admission", "description": "Applications and interviews.", "difficulty": "advanced", "category": "scenario"},
    {"title": "Business Meeting", "description": "Planning, updates, and decisions.", "difficulty": "advanced", "category": "scenario"},
    {"title": "Customer Complaint", "description": "Handling issues and solutions.", "difficulty": "advanced", "category": "scenario"},
    {"title": "AI", "description": "Artificial intelligence and automation.", "difficulty": "intermediate", "category": "technology"},
    {"title": "Startups", "description": "New companies and product ideas.", "difficulty": "advanced", "category": "work"},
    {"title": "Productivity", "description": "Focus, time management, and habits.", "difficulty": "intermediate", "category": "self improvement"},
    {"title": "Communication", "description": "Speaking clearly and listening well.", "difficulty": "intermediate", "category": "self improvement"},
    {"title": "Leadership", "description": "Leading teams and making decisions.", "difficulty": "advanced", "category": "work"},
    {"title": "Environment", "description": "Climate, sustainability, and nature.", "difficulty": "intermediate", "category": "social"},
    {"title": "Science", "description": "Experiments, discovery, and research.", "difficulty": "intermediate", "category": "education"},
    {"title": "History", "description": "Past events and lessons.", "difficulty": "beginner", "category": "education"},
    {"title": "Culture", "description": "Traditions, customs, and identity.", "difficulty": "intermediate", "category": "social"},
    {"title": "Cooking", "description": "Recipes, ingredients, and kitchen talk.", "difficulty": "beginner", "category": "lifestyle"},
    {"title": "Fitness", "description": "Exercise routines and training.", "difficulty": "beginner", "category": "health"},
    {"title": "Shopping Online", "description": "E-commerce and delivery.", "difficulty": "beginner", "category": "daily life"},
    {"title": "News", "description": "Current events and opinions.", "difficulty": "intermediate", "category": "media"},
    {"title": "Movies Review", "description": "Opinionated film discussion.", "difficulty": "intermediate", "category": "entertainment"},
    {"title": "Weekend Plans", "description": "Casual planning and scheduling.", "difficulty": "beginner", "category": "daily life"},
    {"title": "Vacations", "description": "Trips, memories, and experiences.", "difficulty": "beginner", "category": "lifestyle"},
    {"title": "Shopping Returns", "description": "Refunds, exchanges, and customer service.", "difficulty": "intermediate", "category": "scenario"},
    {"title": "Public Speaking", "description": "Presentations and confidence.", "difficulty": "advanced", "category": "work"},
    {"title": "Remote Work", "description": "Working from home and online collaboration.", "difficulty": "intermediate", "category": "work"},
    {"title": "Relationships", "description": "Talking about people and feelings.", "difficulty": "intermediate", "category": "social"},
    {"title": "Goals", "description": "Plans, motivation, and progress.", "difficulty": "beginner", "category": "self improvement"},
]


class Command(BaseCommand):
    help = "Seed the default topic list."

    def handle(self, *args, **options):
        created = 0
        updated = 0
        for topic_data in TOPICS:
            topic, was_created = Topic.objects.update_or_create(
                title=topic_data["title"],
                defaults=topic_data,
            )
            if was_created:
                created += 1
            else:
                updated += 1
        self.stdout.write(self.style.SUCCESS(f"Seeded topics: {created} created, {updated} updated"))
