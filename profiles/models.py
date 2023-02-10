from django.db import models
from account.models import User
from product.models import Product


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites', verbose_name='کاربر')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')

    created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'مورد علاقه'
        verbose_name_plural = 'مورد علاقه ها'

    def __str__(self):
        return f'{self.product} > {self.user}'
