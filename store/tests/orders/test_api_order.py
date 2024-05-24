from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from orders.models import Order, Category
from decimal import Decimal


class OrderAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.order_url = reverse("order-list")
        self.category = Category.objects.create(name="Test Category")
        self.order_id_data = {
            "title": "Test Order",
            "price": "9.99",
            "is_digital": False,
            "description": "A test order.",
            "category": self.category.id,
        }
        self.order_full_data = {
            "title": "Test Order",
            "price": "9.99",
            "is_digital": False,
            "description": "A test order.",
            "category": self.category,
        }

    def test_create_order(self):
        response = self.client.post(self.order_url, self.order_id_data, format="json")
        # if response.status_code != status.HTTP_201_CREATED:
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().title, "Test Order")

    def test_get_orders(self):
        Order.objects.create(
            title="Test Order",
            price=Decimal("9.99"),
            is_digital=False,
            description="A test order.",
            category=self.category,
        )
        Order.objects.create(
            title="Test Order2",
            price=Decimal("9.99"),
            is_digital=False,
            description="A test order.",
            category=self.category,
        )
        response = self.client.get(self.order_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["title"], "Test Order")

    def test_retrieve_orders(self):
        order = Order.objects.create(**self.order_full_data)
        url = reverse("order-detail", kwargs={"pk": order.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # print(response.data)
        self.assertEqual(response.data["title"], "Test Order")

    def test_update_order(self):
        order = Order.objects.create(**self.order_full_data)
        url = reverse("order-detail", kwargs={"pk": order.pk})
        updated_data = {
            "title": "Updated Order",
            "price": "19.99",
            "is_digital": True,
            "description": "An updated test order.",
            "category": self.category.id,
        }
        response = self.client.put(url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        order.refresh_from_db()
        self.assertEqual(order.title, "Updated Order")
        self.assertEqual(order.price, Decimal("19.99"))
        self.assertEqual(order.is_digital, True)

    def test_delete_order(self):
        order = Order.objects.create(**self.order_full_data)
        url = reverse("order-detail", kwargs={"pk": order.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Order.objects.count(), 0)
