from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from orders import views

router = DefaultRouter()
router.register(r"order",views.OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('order/', views.OrderView.as_view()),
    path('', admin.site.urls),
]
