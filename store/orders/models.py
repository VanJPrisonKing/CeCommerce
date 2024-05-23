from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal


class Order(models.Model):
    """
    Order Model
    Defines the attributes of a order
    """

    title = models.CharField(max_length=100)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal("0"))]
    )
    is_digital = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"title: {self.title} price: {self.price} is_digital: {self.is_digital} description: {self.description}"


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
