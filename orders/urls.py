from django.urls import path
from .views import checkout

urlpatterns = [
    path('<pk>', checkout, name='checkout'),
]
