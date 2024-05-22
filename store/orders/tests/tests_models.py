from django.test import TestCase
from ..models import Order

# Create your tests here.


class OrderTest(TestCase):

    def setUp(self):
        # to not rely on external file / 不依赖外部文件
        Order.objects.create(
            title="Hardcore Toy", price=6.66, is_digital=False, description="Gundam model")
        Order.objects.create(
            title="Cute Toy", price=9.99, description="doll")
        Order.objects.create(
            title="Miku Painting", price=233, is_digital=True, description="")

    def test_order_str(self):
        order_gundam = Order.objects.get(title="Hardcore Toy")
        order_doll = Order.objects.get(title="Cute Toy")
        miku_painting = Order.objects.get(price=233)
        self.assertEqual(order_gundam.__str__(), "title: Hardcore Toy price: 6.66 is_digital: False description: Gundam model")
        self.assertEqual(order_doll.__str__(), "title: Cute Toy price: 9.99 is_digital: False description: doll")
        self.assertEqual(miku_painting.__str__(), "title: Miku Painting price: 233.00 is_digital: True description: ")