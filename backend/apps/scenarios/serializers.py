from rest_framework import serializers

from .models import Scenario


class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenario
        fields = [
            "id",
            "title",
            "description",
            "ai_role",
            "user_role",
            "goal",
            "max_turns",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]
