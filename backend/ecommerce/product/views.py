from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .models import Category, Demand
from .serializers import CategorySerializer, DemandSerializer


class CategoryViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing categories
    """

    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)

class DemandViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing demands
    """
    queryset = Demand.objects.all()

    @extend_schema(responses=DemandSerializer)
    def list(self, request):
        serializer = DemandSerializer(self.queryset, many=True)
        return Response(serializer.data)
