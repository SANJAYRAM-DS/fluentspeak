from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User, UserProfile, UserProgress


class RegisterSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=8)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def create(self, validated_data):
        name = validated_data.pop("name")
        user = User.objects.create_user(**validated_data)
        user.profile.full_name = name
        user.profile.save(update_fields=["full_name"])
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(
            request=self.context.get("request"),
            email=attrs["email"],
            password=attrs["password"],
        )
        if not user:
            raise serializers.ValidationError("Invalid email or password.")
        attrs["user"] = user
        return attrs


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["full_name", "avatar_url", "level", "daily_goal", "timezone"]


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ["id", "email", "is_active", "is_verified", "created_at", "profile"]


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["full_name", "avatar_url", "level", "daily_goal", "timezone"]


class AuthTokenSerializer(serializers.Serializer):
    user = UserSerializer()
    refresh = serializers.CharField()
    access = serializers.CharField()

    @staticmethod
    def for_user(user):
        refresh = RefreshToken.for_user(user)
        return {
            "user": UserSerializer(user).data,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }


class UserProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProgress
        fields = [
            "conversations_completed",
            "words_learned",
            "current_streak",
            "total_minutes",
        ]
