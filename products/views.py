from django.shortcuts import render
from .models import Product

# Create your views here.


def products_list(request):
    products = Product.objects.all()
    return render(request, 'products-list.html', {'products': products})
