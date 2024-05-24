from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSimpleSerializer


class UserSimpleView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSimpleSerializer
