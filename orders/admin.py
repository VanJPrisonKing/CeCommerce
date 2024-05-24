from django.contrib import admin

# Register your models here.
from .models import Order, Category

admin.site.register(Order)
admin.site.register(Category)
