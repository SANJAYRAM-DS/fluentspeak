from rest_framework import serializers

from .models import UserVocabulary, VocabularyWord


class VocabularyWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = VocabularyWord
        fields = ["id", "word", "definition", "difficulty", "examples"]


class UserVocabularySerializer(serializers.ModelSerializer):
    vocabulary = VocabularyWordSerializer(read_only=True)

    class Meta:
        model = UserVocabulary
        fields = ["id", "vocabulary", "mastered", "times_seen", "learned_at"]
