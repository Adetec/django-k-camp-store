from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponseBadRequest
from django.contrib.auth.models import User
from .forms import SignUpForm, UpdateProfileForm
from .utils import send_confirmation_email
from .tokens import confirm_email_token_generator

# Create your views here.
def signup(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.is_active = False
            user.save()
            profile_form = UpdateProfileForm(request.POST, instance=user.profile)

            if profile_form.is_valid():
                send_confirmation_email(request, user)
                profile_form.save()
                context = {
                    'user': user
                }
                return render(request, 'registration/signup-successful.html', context)
    else:
        user_form = SignUpForm()
        profile_form = UpdateProfileForm()
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
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
