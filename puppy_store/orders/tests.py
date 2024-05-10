from django.test import TestCase
from .models import Order

# Create your tests here.


class OrderTest(TestCase):

    def setUp(self):
        # to not rely on external file / 不依赖外部文件
        Order.objects.create(title="Hardcore Toy", price=6.66, description="Gundam model")
        Order.objects.create(title="Cute Toy", price=9.99, description="doll")

    def test_order_str(self):
        order_gundam = Order.objects.get(title="Hardcore Toy")
        order_doll = Order.objects.get(title="Cute Toy")
        self.assertEqual(order_gundam.__str__(), "title: Hardcore Toy price: 6.66 description: Gundam model")
        self.assertEqual(order_doll.__str__(), "title: Cute Toy price: 9.99 description: doll")