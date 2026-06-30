from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Conversation
from .serializers import ConversationSerializer, CreateConversationSerializer, SendMessageSerializer
from .services.conversation_service import ConversationService


class ConversationListCreateView(APIView):
    def get(self, request):
        conversations = Conversation.objects.filter(user=request.user)
        return Response(ConversationSerializer(conversations, many=True).data)

    def post(self, request):
        serializer = CreateConversationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = ConversationService.create_conversation(
            request.user,
            topic_id=serializer.validated_data.get("topic_id"),
            scenario_id=serializer.validated_data.get("scenario_id"),
            title=serializer.validated_data.get("title", ""),
        )
        return Response(
            {
                "conversation_id": result["conversation"].id,
                "first_message": result["first_message"],
            },
            status=status.HTTP_201_CREATED,
        )


class ConversationDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = ConversationSerializer

    def get_queryset(self):
        return Conversation.objects.filter(user=self.request.user)


class SendMessageView(APIView):
    def post(self, request, pk):
        serializer = SendMessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = ConversationService.send_message(
            user=request.user,
            conversation_id=pk,
            message=serializer.validated_data["message"],
        )
        return Response(result)
