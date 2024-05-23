from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from ..models import Category


class CategoryAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.category_url = reverse("category-list")
        self.category_data = {"name": "Books"}

    def test_create_category(self):
        response = self.client.post(
            self.category_url, self.category_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        category = Category.objects.get()
        self.assertEqual(category.name, "Books")

    def test_get_categories(self):
        Category.objects.create(name="Books")
        response = self.client.get(self.category_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Books")

    def test_update_category(self):
        category = Category.objects.create(name="Books")
        update_url = reverse("category-detail", kwargs={"pk": category.pk})
        updated_data = {"name": "Updated Books"}
        response = self.client.put(update_url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        category.refresh_from_db()
        self.assertEqual(category.name, "Updated Books")

    def test_delete_category(self):
        category = Category.objects.create(name="Books")
        delete_url = reverse("category-detail", kwargs={"pk": category.pk})
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)
