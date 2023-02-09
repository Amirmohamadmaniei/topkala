from django.db import models

from account.models import User
from product.models import Product


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    full_name = models.CharField(max_length=125)
    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:25]


class Question(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='questions')
    has_parent = models.BooleanField(default=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='answers', null=True, blank=True)
    full_name = models.CharField(max_length=125)
    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:25]

