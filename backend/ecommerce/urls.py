from django.urls import include, path
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# from product import views
from ecommerce.product import views

router = DefaultRouter()
router.register(r"category", views.CategoryViewSet)
router.register(r"demand", views.DemandViewSet)

urlpatterns = [
    # path("", include("orders.urls")),
    # path("api-auth", include("rest_framework.urls", namespace="rest_framework")),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
    path("", admin.site.urls),  # temporary for debug
]
