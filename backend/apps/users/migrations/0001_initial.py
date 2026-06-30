import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("password", models.TextField(db_column="password_hash")),
                ("last_login", models.DateTimeField(blank=True, null=True, verbose_name="last login")),
                ("is_superuser", models.BooleanField(default=False)),
                ("email", models.EmailField(max_length=255, unique=True)),
                ("is_active", models.BooleanField(default=True)),
                ("is_verified", models.BooleanField(default=False)),
                ("is_staff", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("groups", models.ManyToManyField(blank=True, related_name="user_set", related_query_name="user", to="auth.group")),
                ("user_permissions", models.ManyToManyField(blank=True, related_name="user_set", related_query_name="user", to="auth.permission")),
            ],
            options={"db_table": "users"},
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("full_name", models.CharField(blank=True, max_length=100)),
                ("avatar_url", models.TextField(blank=True)),
                ("level", models.CharField(default="beginner", max_length=20)),
                ("daily_goal", models.IntegerField(default=10)),
                ("timezone", models.CharField(default="UTC", max_length=100)),
                ("user", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name="profile", to=settings.AUTH_USER_MODEL)),
            ],
            options={"db_table": "user_profiles"},
        ),
        migrations.CreateModel(
            name="UserProgress",
            fields=[
                ("user", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name="progress", serialize=False, to=settings.AUTH_USER_MODEL)),
                ("conversations_completed", models.IntegerField(default=0)),
                ("words_learned", models.IntegerField(default=0)),
                ("current_streak", models.IntegerField(default=0)),
                ("total_minutes", models.IntegerField(default=0)),
            ],
            options={"db_table": "user_progress"},
        ),
    ]
