from django.contrib import admin

# Register your models here.
from .models import Demand, Category

admin.site.register(Demand)
admin.site.register(Category)
