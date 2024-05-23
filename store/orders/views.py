from django.shortcuts import render
from .models import Order, Category
from .serializers import OrderSerializer, CategorySerializer
from rest_framework.viewsets import ModelViewSet


# class OrderView(GenericViewSet,ListModelMixin,等5项):
class OrderView(ModelViewSet):  # ViewSet重塑了分发机制
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# ===============基于Mixin再封装的接口实现================

# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# class OrderView(ListCreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

# class OrderDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

# class CategoryView(ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class CategoryDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


# ===============基于APIView的接口实现, 最灵活================

# from rest_framework.views import APIView
# from rest_framework.response import Response

# class OrderView(APIView):

#     def get(self, request):
#         order_list = Order.objects.all()
#         serializer = OrderSerializer(instance=order_list, many=True)
#         return Response(serializer.data)
#         # return HttpResponse(serializer.data)

#     def post(self, request):
#         print("data", request.data)
#         # 接收到数据但不一定合法
#         serializer = OrderSerializer(data=request.data)
#         # 校验数据
#         if serializer.is_valid():  # 所有字段皆通过才返回True
#             # 数据校验通过 serializer.validated_data   serialzer.errors
#             serializer.save()  # Order.objects.create(**serializer.validated_data)
#             return Response(serializer.data)
#         else:
#             # 校验失败
#             return Response(serializer.errors)


# class OrderDetailView(APIView):
#     def get(self, request, id):
#         order = Order.objects.get(pk=id)
#         serializer = OrderSerializer(instance=order, many=False)
#         return Response(serializer.data)

#     def put(self, request, id):
#         print("data", request.data)
#         order = Order.objects.get(pk=id)
#         serializer = OrderSerializer(instance=order, data=request.data)
#         # 校验数据
#         if serializer.is_valid():
#             serializer.save()  # update
#             return Response(serializer.data)
#         else:
#             # 校验失败
#             return Response(serializer.errors)

#     def delete(self, request, id):
#         order = Order.objects.get(pk=id).delete()
#         return Response()
