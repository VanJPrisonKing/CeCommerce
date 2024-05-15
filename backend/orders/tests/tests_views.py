import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Order
from ..serializers import OrderSerializer

# initialize the APIClient app
client = Client()


class GetAllOrdersTest(TestCase):
    """Test module for GET all Orders API"""

    def setUp(self):
        Order.objects.create(
            title="Hardcore Toy", price=6.66, description="Gundam model"
        )
        Order.objects.create(title="Cute Toy", price=9.99, description="doll")
        Order.objects.create(title="Tissue", price=0.5, description="paper towel")
        Order.objects.create(
            title="Game Concept Design",
            price=233,
            description="Elden Ring Concept Design Book",
        )

    def test_get_all_Orders(self):
        # get API response
        response = client.get(reverse("get_post_orders"))
        # get data from db
        Orders = Order.objects.all()
        serializer = OrderSerializer(Orders, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleOrderTest(TestCase):
    """Test module for GET single Order API"""

    def setUp(self):
        Order.objects.create(
            title="Hardcore Toy", price=6.66, description="Gundam model"
        )
        Order.objects.create(title="Cute Toy", price=9.99, description="doll")
        self.tissue = Order.objects.create(
            title="Tissue", price=0.5, description="paper towel"
        )
        Order.objects.create(
            title="Game Concept Design",
            price=233,
            description="Elden Ring Concept Design Book",
        )

    def test_get_valid_single_Order(self):
        response = client.get(
            reverse("get_delete_update_order", kwargs={"pk": self.tissue.pk})
        )
        order = Order.objects.get(pk=self.tissue.pk)
        serializer = OrderSerializer(order)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_Order(self):
        response = client.get(reverse("get_delete_update_order", kwargs={"pk": 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewOrderTest(TestCase):
    """Test module for inserting a new Order"""

    def setUp(self):
        self.valid_payload = {
            "title": "Tissue",
            "price": 0.5,
            "description": "paper towel",
        }
        self.untitled_payload = {
            "title": "",
            "price": 0.5,
            "description": "paper towel",
        }
        self.negative_price_payload = {
            "title": "Tissue",
            "price": -1,
            "description": "paper towel",
        }

    def test_create_valid_Order(self):
        response = client.post(
            reverse("get_post_orders"),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_untitled_Order(self):
        response = client.post(
            reverse("get_post_orders"),
            data=json.dumps(self.untitled_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_negative_price_Order(self):
        response = client.post(
            reverse("get_post_orders"),
            data=json.dumps(self.negative_price_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleOrderTest(TestCase):
    """Test module for updating an existing order record"""

    def setUp(self):
        self.gundam = Order.objects.create(
            title="Hardcore Toy", price=6.66, description="Gundam model"
        )
        self.doll = Order.objects.create(
            title="Cute Toy", price=9.99, description="doll"
        )
        self.valid_payload = {
            "title": "Gundam",
            "price": 2.33,
            "description": "Gundam model",
        }
        self.untitled_payload = {
            "title": "",
            "price": 0.5,
            "description": "doll",
        }
        self.negative_price_payload = {
            "title": "Cute Doll",
            "price": -1,
            "description": "doll",
        }

    def test_valid_update_order(self):
        response = client.put(
            reverse("get_delete_update_order", kwargs={"pk": self.gundam.pk}),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_untitled_update_order(self):
        response = client.put(
            reverse("get_delete_update_order", kwargs={"pk": self.doll.pk}),
            data=json.dumps(self.untitled_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_price_update_order(self):
        response = client.put(
            reverse("get_delete_update_order", kwargs={"pk": self.doll.pk}),
            data=json.dumps(self.negative_price_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleOrderTest(TestCase):
    """Test module for deleting an existing order record"""

    def setUp(self):
        self.gundam = Order.objects.create(
            title="Hardcore Toy", price=6.66, description="Gundam model"
        )
        self.doll = Order.objects.create(
            title="Cute Toy", price=9.99, description="doll"
        )

    def test_valid_delete_order(self):
        response = client.delete(
            reverse("get_delete_update_order", kwargs={"pk": self.gundam.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_order(self):
        response = client.delete(reverse("get_delete_update_order", kwargs={"pk": 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
