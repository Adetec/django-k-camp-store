from django.shortcuts import render, redirect
from .forms import SignUpForm
from .utils import send_confirmation_email

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            send_confirmation_email(user)
            context = {
                'user': user
            }
            return render(request, 'registration/signup-successful.html', context)
    else:
        form = SignUpForm()
    context = {
        'form': form,
        'operation': {
            'title': 'signup',
            'description': 'Please fill in this form to create your account.'
        }
    }
    return render(request, 'registration/signup.html', context )