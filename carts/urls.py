from django.urls import path
from .views import add_to_cart, cart, remove_from_cart, remove_all_from_cart


urlpatterns = [
    path('carts/remove_all_from_cart', remove_all_from_cart, name='remove_all_from_cart'),
    path('carts/', cart, name='cart'),
    path('carts/add/<int:product_id>', add_to_cart, name='add_to_cart'),
    path('carts/remove_from_cart/<int:product_id>', remove_from_cart, name='remove_from_cart'),
]
