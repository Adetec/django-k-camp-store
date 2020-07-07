from django.urls import path
from .views import products_list, product_details, product_add

urlpatterns = [
    path('products/', products_list, name='products_list'),
    path('products/<pk>', product_details, name='product_details'),
    path('products/new/add', product_add, name='product_add')
]
