from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate


class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        # fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}


class UserLoginSerializer(serializers.Serializer):
    username_or_email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username_or_email = data.get("username_or_email")
        password = data.get("password")
        if not (username_or_email and password):
            raise serializers.ValidationError(
                "Both username/email and password are required."
            )
        return data
