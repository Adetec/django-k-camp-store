from django.shortcuts import render, get_object_or_404, redirect
from carts.models import Cart
from accounts.models import Profile
from .models import Order
from .forms import OrderForm
from .utils import send_order_email


# Create your views here.

def checkout(request, pk):
    user = request.user
    if user.is_authenticated:
        
        cart = user.cart
        profile = Profile.objects.filter(user_id=user.id).first()
        
        if request.method == 'POST':
            form = OrderForm(request.POST)

            if form.is_valid():
                form.save_order(user)

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
