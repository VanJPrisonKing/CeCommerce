from django.urls import path
from django.contrib import admin

from orders import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('order/', views.OrderView.as_view()),
    path('', admin.site.urls),
]
