from rest_framework.test import APITestCase
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken


class AuthFlowTests(APITestCase):
    def test_register_login_me_and_logout_blacklists_refresh(self):
        register_response = self.client.post(
            "/api/v1/auth/register",
            {
                "name": "Sanjay",
                "email": "sanjay@example.com",
                "password": "password123",
            },
            format="json",
        )
        self.assertEqual(register_response.status_code, 201)

        access_token = register_response.data["access"]
        refresh_token = register_response.data["refresh"]

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
        me_response = self.client.get("/api/v1/me")
        self.assertEqual(me_response.status_code, 200)
        self.assertEqual(me_response.data["email"], "sanjay@example.com")

        logout_response = self.client.post(
            "/api/v1/auth/logout",
            {"refresh": refresh_token},
            format="json",
        )
        self.assertEqual(logout_response.status_code, 200)
        self.assertEqual(BlacklistedToken.objects.count(), 1)
