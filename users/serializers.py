from django.contrib.auth.models import User
from rest_framework import serializers


class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        # fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}
