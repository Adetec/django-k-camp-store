from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.


def products_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/products-list.html', context)


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'products/product-details.html', context)


def product_add(request):
    return render(request, 'products/product-add.html')
