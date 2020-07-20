from django.urls import path
from .views import checkout

urlpatterns = [
    path('orders/<int:pk>', checkout, name='checkout'),
]
