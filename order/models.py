from django.db import models
from account.models import User
from home.models import Post
from product.models import Product, Color
from django.core.validators import MaxValueValidator, MinValueValidator


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name='کاربر')
    is_paid = models.BooleanField(default=False, verbose_name='پرداخت شذه')

    f_name = models.CharField(max_length=90, verbose_name='نام')
    l_name = models.CharField(max_length=90, verbose_name='نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    phone = models.CharField(max_length=11, verbose_name='موبایل')
    address = models.TextField(verbose_name='آدرس')
    postal_code = models.CharField(max_length=10, verbose_name='کد پستی')

    discount = models.IntegerField(blank=True, null=True, default=None, verbose_name='تخفیف')

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارش ها'

    @property
    def get_count_item(self):
        return self.items.count()

    @property
    def get_total_price(self):
        total = sum(item.get_total_price for item in self.items.all())
        if self.discount:
            total = total - ((total * self.discount) // 100)
        return total

    @property
    def get_total_price_with_post(self):
        post_cost = Post.objects.all().last()
        total = sum(item.get_total_price for item in self.items.all())
        if self.discount:
            if self.discount:
                total = total - ((total * self.discount) // 100)
        return total + post_cost.cost

    def get_discount(self):
        total = sum(item.get_total_price for item in self.items.all())
        return (total * self.discount) // 100


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name='سفارش')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    quantity = models.SmallIntegerField(default=1, verbose_name='تعداد')
    color = models.ManyToManyField(Color, verbose_name='رنگ')
    price_with_discount = models.PositiveIntegerField(verbose_name='قیمت (با تخفیف)')

    class Meta:
        verbose_name = 'ایتم سفارش'
        verbose_name_plural = 'ایتم های سفارش'

    def __str__(self):
        return self.product.title

    @property
    def get_total_price(self):
        return self.price_with_discount * self.quantity


class Coupon(models.Model):
    code = models.CharField(max_length=12, unique=True, verbose_name='کد')
    discount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(90)], verbose_name='درصد تخفیف')

    valid_from = models.DateTimeField(verbose_name='معتبر از')
    valid_to = models.DateTimeField(verbose_name='معتبر تا')

    active = models.BooleanField(default=False, verbose_name='فعال')

    class Meta:
        verbose_name = 'کد تخفیف'
        verbose_name_plural = 'کد های تخفیف'

    def __str__(self):
        return f'{self.code} - {self.discount}%'
