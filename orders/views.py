from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User


# Create your views here.
def checkout(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'orders/order.html', {'user': user})
