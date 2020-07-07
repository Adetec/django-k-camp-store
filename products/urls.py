from django.urls import path
from .views import products_list, product_details, product_add, product_edit

urlpatterns = [
    path('products/', products_list, name='products_list'),
    path('products/add', product_add, name='product_add'),
    path('products/edit/<pk>', product_edit, name='product_edit'),
    path('products/<pk>', product_details, name='product_details'),
]
