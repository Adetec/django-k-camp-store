from django.shortcuts import render, get_object_or_404, redirect
from carts.models import Cart
from accounts.models import Profile
from .models import Order
from django.db.models import Sum
from .forms import OrderForm
from .utils import send_confirmation_email


# Create your views here.

def checkout(request, pk):
    user = request.user
    if user.is_authenticated:
        
        cart = user.cart
        profile = Profile.objects.filter(user_id=user.id).first()
        products = cart.items.all()
        
        if request.method == 'POST':
            order = Order(
                user=user,
                address=profile.address,
            )
            form = OrderForm(request.POST, instance=order)

            if form.is_valid():
                form.save()
                order.items.set(products)
                total_price = products.aggregate(Sum('price'))
                send_confirmation_email(order, total_price)

                return render(request, 'orders/order-successful.html')
        else:
            form = OrderForm(initial={
                'address': profile.address
            })
            context = {
                'form': form,
                'cart': cart,
                }
            
            return render(request, 'orders/order.html', context)
    else:
        return redirect('login')
