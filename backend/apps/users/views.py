from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from .models import UserProfile, UserProgress
from .serializers import (
    AuthTokenSerializer,
    LoginSerializer,
    RegisterSerializer,
    UserProfileUpdateSerializer,
    UserProgressSerializer,
    UserSerializer,
)


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(AuthTokenSerializer.for_user(user), status=status.HTTP_201_CREATED)


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        return Response(AuthTokenSerializer.for_user(serializer.validated_data["user"]))


class LogoutView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        refresh_token = request.data.get("refresh")
        if refresh_token:
            try:
                RefreshToken(refresh_token).blacklist()
            except TokenError:
                return Response({"detail": "Invalid refresh token."}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"detail": "Logged out."}, status=status.HTTP_200_OK)


class MeView(APIView):
    def get(self, request):
        return Response(UserSerializer(request.user).data)

    def patch(self, request):
        profile, _ = UserProfile.objects.get_or_create(user=request.user)
        serializer = UserProfileUpdateSerializer(
            instance=profile,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(UserSerializer(request.user).data)


class UserProgressView(APIView):
    def get(self, request):
        progress, _ = UserProgress.objects.get_or_create(user=request.user)
        return Response(UserProgressSerializer(progress).data)
