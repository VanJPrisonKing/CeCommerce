from rest_framework import viewsets, status
from django.contrib.auth.models import User
from .serializers import (
    UserSimpleSerializer,
    UserLoginSerializer,
    UserSignupSerializer,
)
from rest_framework.response import Response
from django.contrib.auth import authenticate


class UserSimpleView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSimpleSerializer


class UserLoginView(viewsets.ViewSet):
    serializer_class = UserLoginSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get("username")
            password = serializer.validated_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                return Response(
                    {"message": "Login successful"}, status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"message": "Invalid credentials"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserSignupView(viewsets.ViewSet):
    serializer_class = UserSignupSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {"message": "User created successfully", "user_id": user.id},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
