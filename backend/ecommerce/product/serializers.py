from rest_framework import serializers

from .models import Demand, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class DemandSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Demand
        fields = "__all__"

