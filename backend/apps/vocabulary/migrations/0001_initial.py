import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="VocabularyWord",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("word", models.CharField(max_length=100, unique=True)),
                ("definition", models.TextField()),
                ("difficulty", models.CharField(blank=True, max_length=20)),
                ("examples", models.JSONField(blank=True, default=list)),
            ],
            options={"db_table": "vocabulary_words", "ordering": ["word"]},
        ),
        migrations.CreateModel(
            name="UserVocabulary",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("mastered", models.BooleanField(default=False)),
                ("times_seen", models.IntegerField(default=0)),
                ("learned_at", models.DateTimeField(auto_now_add=True)),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="vocabulary_items", to=settings.AUTH_USER_MODEL)),
                ("vocabulary", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="user_items", to="vocabulary.vocabularyword")),
            ],
            options={"db_table": "user_vocabulary", "unique_together": {("user", "vocabulary")}},
        ),
    ]
