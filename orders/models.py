from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)
    ordered_at = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=500, default='')


    def __str__(self):
        return f'{self.user.username}\'s order'
