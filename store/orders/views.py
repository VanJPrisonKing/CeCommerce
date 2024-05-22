from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer

# CBV
# from django.views import View
from rest_framework.views import APIView

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
        #校验数据
        if serializer.is_valid(): #所有字段皆通过才返回True   serializer.validated_data   serialzer.errors
            # 数据校验通过
            Order.objects.create(**serializer.validated_data)
            return Response(serializer.data)
        else:
            # 校验失败
            return Response(serializer.errors)

    def delete(self, request):
        return Response("DELETE请求...")

# FBV 

# @api_view(['GET', 'POST'])
# def get_post_orders(request):
#      # get all orders
#     if request.method == 'GET':
#         orders = Order.objects.all()
#         serializer = OrderSerializer(orders, many=True)
#         return Response(serializer.data)
#     # insert a new record for a order
#     if request.method == 'POST':
#         data = {
#             'title': request.data.get('title'),
#             'price': float(request.data.get('price')),
#             'description': request.data.get('description'),
#         }
#         serializer = OrderSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'DELETE', 'PUT'])
# def get_delete_update_order(request, pk):
#     try:
#         order = Order.objects.get(pk=pk)
#     except Order.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     # get details of a single order
#     if request.method == 'GET':
#         serializer = OrderSerializer(order)
#         return Response(serializer.data)
#     # update details of a single order
#     elif request.method == 'PUT':
#         serializer = OrderSerializer(order, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     # delete a single order
#     elif request.method == 'DELETE':
#         order.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)