import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AIProvider",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                ("model", models.CharField(max_length=50)),
                ("priority", models.IntegerField(default=100)),
                ("status", models.CharField(default="active", max_length=20)),
            ],
            options={"db_table": "ai_providers", "ordering": ["priority", "name"]},
        ),
    ]
