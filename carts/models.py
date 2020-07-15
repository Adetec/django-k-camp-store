from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product


User = get_user_model()
# Create your models here.

class Cart(models.Model):
    user = models.OneToOneField(User, related_name='cart', on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username}\'s cart'
