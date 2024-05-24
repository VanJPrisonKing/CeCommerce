# orders/urls.py
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("order", views.OrderView)
router.register("category", views.CategoryView)

urlpatterns = router.urls
