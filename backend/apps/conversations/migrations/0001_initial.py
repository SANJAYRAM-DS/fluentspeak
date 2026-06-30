import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("topics", "0001_initial"),
        ("scenarios", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Conversation",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(blank=True, max_length=255)),
                ("status", models.CharField(default="active", max_length=20)),
                ("current_turn", models.IntegerField(default=0)),
                ("summary", models.TextField(blank=True)),
                ("scenario", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="conversations", to="scenarios.scenario")),
                ("topic", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="conversations", to="topics.topic")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="conversations", to=settings.AUTH_USER_MODEL)),
            ],
            options={"db_table": "conversations", "ordering": ["-updated_at"]},
        ),
        migrations.CreateModel(
            name="ConversationState",
            fields=[
                ("conversation", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name="state", serialize=False, to="conversations.conversation")),
                ("stage", models.CharField(default="opening", max_length=30)),
                ("tone", models.CharField(default="friendly", max_length=30)),
                ("goal_progress", models.IntegerField(default=0)),
                ("last_vocab_word", models.CharField(blank=True, max_length=100)),
                ("summary", models.TextField(blank=True)),
            ],
            options={"db_table": "conversation_states"},
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("role", models.CharField(choices=[("user", "User"), ("assistant", "Assistant"), ("system", "System")], max_length=20)),
                ("content", models.TextField()),
                ("turn_number", models.IntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("conversation", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="messages", to="conversations.conversation")),
            ],
            options={"db_table": "messages", "ordering": ["created_at"]},
        ),
        migrations.CreateModel(
            name="MessageFeedback",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("correction", models.TextField(blank=True)),
                ("optimized_response", models.TextField(blank=True)),
                ("next_question", models.TextField(blank=True)),
                ("message", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name="feedback", to="conversations.message")),
            ],
            options={"db_table": "message_feedback"},
        ),
    ]
