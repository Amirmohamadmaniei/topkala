from django.db import models
from account.models import User
from product.models import Product, Color


class Order(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='order')
    item = models.ForeignKey('OrderItem', on_delete=models.CASCADE)

    is_paid = models.BooleanField(default=False)

    total_price = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.phone


class OrderItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    color = models.ManyToManyField(Color)
    price_with_discount = models.IntegerField()

    def __str__(self):
        return self.product.title
