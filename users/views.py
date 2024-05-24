from rest_framework import viewsets, status
from django.contrib.auth.models import User
from .serializers import UserSimpleSerializer, UserLoginSerializer
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
            username_or_email = serializer.validated_data.get("username_or_email")
            password = serializer.validated_data.get("password")
            if "@" in username_or_email:
                user = authenticate(request, email=username_or_email, password=password)
            else:  # 否则，使用用户名进行验证
                user = authenticate(username=username_or_email, password=password)
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
