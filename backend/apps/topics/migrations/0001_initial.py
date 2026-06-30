import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Topic",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=100, unique=True)),
                ("description", models.TextField(blank=True)),
                ("difficulty", models.CharField(blank=True, max_length=20)),
                ("category", models.CharField(blank=True, max_length=50)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={"db_table": "topics", "ordering": ["title"]},
        ),
    ]
