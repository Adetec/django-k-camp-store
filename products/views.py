from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import AddProductForm

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
        form = AddProductForm(request.POST)

        if form.is_valid():
            product.save()
            return render(request, 'products/product-add-successful.html')
    else:
        form = AddProductForm()

    return render(request, 'products/product-add.html', {'form': form})
