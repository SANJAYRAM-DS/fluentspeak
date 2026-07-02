from unittest.mock import patch

from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from apps.ai.services.groq_client import GroqResult
from apps.conversations.models import Conversation, Message
from apps.topics.models import Topic


class ConversationTurnTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(email="learner@example.com", password="password123")
        topic = Topic.objects.create(
            title="Travel",
            description="Trips and transport",
            difficulty="beginner",
            category="lifestyle",
        )
        register_response = self.client.post(
            "/api/v1/auth/login",
            {"email": "learner@example.com", "password": "password123"},
            format="json",
        )
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {register_response.data['access']}")
        create_response = self.client.post("/api/v1/conversations", {"topic_id": str(topic.id)}, format="json")
        self.conversation_id = create_response.data["conversation_id"]

    @patch("apps.ai.services.groq_client.GroqClient.complete_json")
    def test_turn_endpoint_generates_reply(self, mock_complete_json):
        mock_complete_json.return_value = GroqResult(
            provider="groq",
            model="llama-3.1-70b-versatile",
            content=(
                '{"reply":"What did you see?","correction":"I went to the market yesterday.",'
                '"optimized_response":"I went to the market yesterday and bought fruit.",'
                '"vocabulary":{"word":"fresh","definition":"recently made","examples":["Fresh fruit is tasty."]},'
                '"examples":["Fresh fruit is tasty."],"next_question":"What did you buy?"}'
            ),
            token_count=120,
            latency_ms=45,
        )

        response = self.client.post(
            f"/api/v1/conversations/{self.conversation_id}/turns",
            {"message": "I go market yesterday"},
            format="json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["reply"], "What did you see?")
        self.assertEqual(Message.objects.filter(conversation_id=self.conversation_id).count(), 3)
        self.assertEqual(Conversation.objects.get(id=self.conversation_id).current_turn, 1)
