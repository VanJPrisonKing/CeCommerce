from rest_framework.test import APITestCase
from ..models import Order, Category

# Create your tests here.


class OrderTest(APITestCase):

    def setUp(self):
        # to not rely on external file / 不依赖外部文件
        Order.objects.create(
            title="Hardcore Toy",
            price=6.66,
            is_digital=False,
            description="Gundam model",
        )
        Order.objects.create(title="Cute Toy", price=9.99, description="doll")
        Order.objects.create(
            title="Miku Painting", price=233, is_digital=True, description=""
        )

    def test_order_str(self):
        order_gundam = Order.objects.get(title="Hardcore Toy")
        order_doll = Order.objects.get(title="Cute Toy")
        miku_painting = Order.objects.get(price=233)
        self.assertEqual(
            order_gundam.__str__(),
            "Hardcore Toy",
        )
        self.assertEqual(
            order_doll.__str__(),
            "Cute Toy",
        )
        self.assertEqual(
            miku_painting.__str__(),
            "Miku Painting",
        )


class CategoryTest(APITestCase):
    def setUp(self):
        Category.objects.create(name="food")

    def test_category_str(self):
        category_food = Category.objects.get(name="food")
        self.assertEqual(category_food.__str__(), "food")
