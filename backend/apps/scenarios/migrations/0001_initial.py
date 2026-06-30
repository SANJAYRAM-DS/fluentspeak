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
            name="Scenario",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=150)),
                ("description", models.TextField(blank=True)),
                ("ai_role", models.CharField(max_length=100)),
                ("user_role", models.CharField(max_length=100)),
                ("goal", models.TextField(blank=True)),
                ("max_turns", models.IntegerField(default=10)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="scenarios", to=settings.AUTH_USER_MODEL)),
            ],
            options={"db_table": "scenarios", "ordering": ["-created_at"]},
        ),
    ]
