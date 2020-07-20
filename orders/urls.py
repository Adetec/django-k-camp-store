from django.urls import path
from .views import checkout, order_list

urlpatterns = [
    path('orders/', order_list, name='order_list'),
    path('orders/<int:pk>', checkout, name='checkout'),
]
