from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.


def products_list(request):
    products = Product.objects.all()
    return render(request, 'products-list.html', {'products': products})


def product_details(request, id):
    product = get_object_or_404(Product, id)
    return render(request, 'product-details.html', {'product': product})
