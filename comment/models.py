from django.db import models
from product.models import Product


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', verbose_name='محصول')
    full_name = models.CharField(max_length=125, verbose_name='نام و نام خانوادگی')
    body = models.TextField(verbose_name='متن')

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'نطر'
        verbose_name_plural = 'نطرات'

    def __str__(self):
        return self.body[0:25]


class Question(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='questions', verbose_name='محصول')
    has_parent = models.BooleanField(default=False, verbose_name='دارای والد ؟')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='answers', null=True, blank=True,
                               verbose_name='والد')
    full_name = models.CharField(max_length=125, verbose_name='نام و نام خانوادگی')
    body = models.TextField(verbose_name='متن')

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'پرسش و پاسخ'
        verbose_name_plural = 'پرسش و پاسخ ها'

    def __str__(self):
        return self.body[0:25]
