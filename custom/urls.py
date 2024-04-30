from django.urls import path

from . import views

app_name = "custom"
urlpatterns = [
    # ex: /custom/
    path("", views.index, name="index"),
    # ex: /custom/5/
    path("<int:order_id>/", views.detail, name="detail"),
]