from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
# Create your models here.
class Order(models.Model):
    """
    Order Model
    Defines the attributes of a order
    """
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0'))])
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"title: {self.title} price: {self.price} description: {self.description}"