from django.http import StreamingHttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Conversation
from .serializers import (
    ConversationSerializer,
    CreateConversationSerializer,
    SendMessageSerializer,
    TurnResponseSerializer,
)
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


class ConversationSwitchView(APIView):
    def post(self, request, pk):
        conversation = get_object_or_404(Conversation, id=pk, user=request.user)
        if request.data.get("topic_id"):
            conversation.topic_id = request.data["topic_id"]
        if request.data.get("scenario_id"):
            conversation.scenario_id = request.data["scenario_id"]
        conversation.save(update_fields=["topic", "scenario", "updated_at"])
        return Response(ConversationSerializer(conversation).data)


class ConversationMessageListView(APIView):
    def get(self, request, pk):
        conversation = get_object_or_404(Conversation, id=pk, user=request.user)
        messages = [
            {
                "id": message.id,
                "role": message.role,
                "content": message.content,
                "turn_number": message.turn_number,
                "created_at": message.created_at,
            }
            for message in conversation.messages.all()
        ]
        return Response({"messages": messages})


class ConversationTurnView(APIView):
    def post(self, request, pk):
        serializer = SendMessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = ConversationService.generate_turn(
            user=request.user,
            conversation_id=pk,
            message=serializer.validated_data["message"],
            client_message_id=serializer.validated_data.get("client_message_id"),
            conversation_revision=serializer.validated_data.get("conversation_revision"),
        )
        return Response(TurnResponseSerializer(result).data)


class ConversationTurnStreamView(APIView):
    def get(self, request, pk):
        message = request.query_params.get("message", "")
        response = StreamingHttpResponse(
            ConversationService.stream_turn(request.user, pk, message),
            content_type="text/event-stream",
        )
        response["Cache-Control"] = "no-cache"
        response["X-Accel-Buffering"] = "no"
        return response


class ConversationTurnDetailView(APIView):
    def get(self, request, pk, turn_pk):
        conversation = get_object_or_404(Conversation, id=pk, user=request.user)
        message = conversation.messages.get(id=turn_pk)
        response = {
            "turn_id": message.id,
            "conversation_id": conversation.id,
            "reply": message.content,
            "conversation_revision": message.turn_number,
        }
        if hasattr(message, "feedback"):
            response.update(
                {
                    "correction": message.feedback.correction,
                    "optimized_response": message.feedback.optimized_response,
                    "next_question": message.feedback.next_question,
                }
            )
        return Response(response)
