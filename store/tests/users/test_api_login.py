from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse


class UserLoginTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.login_url = reverse("user-login-list")
        self.user = User.objects.create_user(
            username="testuser", email="testuser@example.com", password="testpassword"
        )

    def test_valid_login(self):
        data = {"username_or_email": "testuser", "password": "testpassword"}
        response = self.client.post(self.login_url, data, format="json")
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Login successful")

    def test_valid_email_login(self):
        data = {"username_or_email": "testuser@example.com", "password": "testpassword"}
        response = self.client.post(self.login_url, data, format="json")
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Login successful")

    def test_invalid_credentials(self):
        data = {
            "username_or_email": "testuser@example.com",
            "password": "invalidpassword",
        }
        response = self.client.post(self.login_url, data, format="json")
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data["message"], "Invalid credentials")

    def test_missing_username_or_email(self):
        data = {"password": "testpassword"}
        response = self.client.post(self.login_url, data, format="json")
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_password(self):
        data = {"username_or_email": "testuser"}
        response = self.client.post(self.login_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
