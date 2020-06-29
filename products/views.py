from django.shortcuts import render

# Create your views here.


def say_hi(request, name):
    return render(request, 'say-hi.html', {'name': name})
