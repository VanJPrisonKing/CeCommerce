from django.shortcuts import render
from rest_framework.response import Response
from .models import Order

# from .serializers import OrderSerializer
from rest_framework import serializers

# CBV
# from django.views import View
from rest_framework.views import APIView


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderView(APIView):

    def get(self, request):
        order_list = Order.objects.all()
        serializer = OrderSerializer(instance=order_list, many=True)
        return Response(serializer.data)
        # return HttpResponse(serializer.data)

    def post(self, request):
        print("data", request.data)
        # 接收到数据但不一定合法
        serializer = OrderSerializer(data=request.data)
        # 校验数据
        if serializer.is_valid():  # 所有字段皆通过才返回True
            # 数据校验通过 serializer.validated_data   serialzer.errors
            serializer.save()  # Order.objects.create(**serializer.validated_data)
            return Response(serializer.data)
        else:
            # 校验失败
            return Response(serializer.errors)


class OrderDetailView(APIView):
    def get(self, request, id):
        order = Order.objects.get(pk=id)
        serializer = OrderSerializer(instance=order, many=False)
        return Response(serializer.data)

    def put(self, request, id):
        print("data", request.data)
        order = Order.objects.get(pk=id)
        serializer = OrderSerializer(instance=order, data=request.data)
        # 校验数据
        if serializer.is_valid():
            serializer.save()  # update
            return Response(serializer.data)
        else:
            # 校验失败
            return Response(serializer.errors)

    def delete(self, request, id):
        order = Order.objects.get(pk=id).delete()
        return Response()
