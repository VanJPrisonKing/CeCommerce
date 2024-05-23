from django.urls import path, include
from django.contrib import admin

from rest_framework.routers import DefaultRouter
from orders import views

router = DefaultRouter()
router.register("order", views.OrderView)
router.register("category", views.CategoryView)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("", admin.site.urls),  # temporary for debug
]
