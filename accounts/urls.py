from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup

urlpatterns = [
    path('signup', signup, name='signup'),
    path('login', auth_views.LoginView, name='login'),
    path('logout', auth_views.LogoutView, name='logout')
]
