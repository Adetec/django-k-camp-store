from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from .models import Cart
from django.contrib.auth.decorators import login_required
from django.db.models import Sum


# Create your views here.
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = Cart.objects.get(user= request.user)

    cart.items.add(product)

    return redirect('cart')


@login_required
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = Cart.objects.get(user= request.user)

    cart.items.remove(product)

    return redirect('cart')


@login_required
def remove_all_from_cart(request): 
    cart = request.user.cart
    cart.items.clear()

    return redirect('cart')


@login_required
def cart(request):
    user = request.user
    products = user.cart.items.all()

    total_price = products.aggregate(Sum('price'))
    context = {
        'products': products,
        'total_price': total_price
    }

    return render(request, 'carts/cart.html', context)
