from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponseBadRequest
from django.contrib.auth.models import User
from .forms import SignUpForm
from .utils import send_confirmation_email
from .tokens import confirm_email_token_generator

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            send_confirmation_email(request, user)
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


def activate_email(request, uid, token):
    user = get_object_or_404(User, pk=uid)

    if confirm_email_token_generator.check_token(user, token):
        user.is_active = True
        user.save()

        return redirect('login')
    else:
        return HttpResponseBadRequest('Bad token')
