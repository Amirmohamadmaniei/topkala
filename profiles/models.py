from django.db import models
from account.models import User
from product.models import Product


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.product} > {self.user}'
