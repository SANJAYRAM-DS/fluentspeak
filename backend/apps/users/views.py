from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserProgress
from .serializers import AuthTokenSerializer, LoginSerializer, RegisterSerializer, UserProgressSerializer


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


class UserProgressView(APIView):
    def get(self, request):
        progress, _ = UserProgress.objects.get_or_create(user=request.user)
        return Response(UserProgressSerializer(progress).data)
