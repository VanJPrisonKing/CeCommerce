from django.urls import path, include
from django.contrib import admin
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from orders.views import OrderView, CategoryView
from users.views import UserSimpleView

router = DefaultRouter()
router.register("order", OrderView)
router.register("category", CategoryView)
router.register("user", UserSimpleView)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    # path("api/", include("users.urls")),
    path("swagger/", SpectacularSwaggerView.as_view(url_name="schema")),
    path("swagger/doc/", SpectacularAPIView.as_view(), name="schema"),
    # path("", admin.site.urls),  # temporary for debug
]
