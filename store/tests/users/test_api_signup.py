from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from users.serializers import UserSignupSerializer


class UserSignupTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse("user-signup-list")
        self.valid_payload = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpassword",
        }
        self.invalid_payload = {
            "username": "testuser",
            "email": "invalid_email",  # 无效的电子邮件格式
            "password": "testpassword",
        }

    def test_valid_signup(self):
        response = self.client.post(
            self.register_url, self.valid_payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, "testuser")

    def test_invalid_signup(self):
        response = self.client.post(
            self.register_url, self.invalid_payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)
