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
    if request.method == 'POST':
        brand = request.POST['brand']
        title = request.POST['title']
        description = request.POST['description']
        price = request.POST['price']

        product = Product(
            brand=brand,
            title=title,
            description=description,
            price=price
        )
        product.save()
        return render(request, 'products/product-add-successful.html')
    else:
        return render(request, 'products/product-add.html')
