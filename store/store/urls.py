from django.urls import path, re_path
from django.contrib import admin

# from rest_framework.routers import DefaultRouter
from orders import views

# router = DefaultRouter()
# router.register(r"order",views.OrderViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('api/', include(router.urls)),
    path("order/", views.OrderView.as_view()),
    re_path("order/(?P<pk>\d+)", views.OrderDetailView.as_view()),
    path("category/", views.CategoryView.as_view()),
    re_path("category/(?P<pk>\d+)", views.CategoryDetailView.as_view()),
    path("", admin.site.urls),
]
