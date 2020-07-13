from django.shortcuts import render, redirect
from .forms import SignUpForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
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