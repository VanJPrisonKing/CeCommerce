from rest_framework import serializers
from .models import Order


class PuppySerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('title', 'price', 'description', 'created_at', 'updated_at')