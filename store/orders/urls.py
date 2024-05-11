from django.urls import path
from . import views


urlpatterns = [
    path(
        'api/v1/orders/<int:pk>',
        views.get_delete_update_order,
        name='get_delete_update_order'
    ),
    path(
        'api/v1/orders/',
        views.get_post_orders,
        name='get_post_orders'
    )
]