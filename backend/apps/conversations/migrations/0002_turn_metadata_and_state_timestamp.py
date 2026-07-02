from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("conversations", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="token_count",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="message",
            name="latency_ms",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="message",
            name="provider",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name="message",
            name="model",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name="conversationstate",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
