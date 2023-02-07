from django.db import models
from account.models import User
from home.models import Post
from product.models import Product, Color
from django.core.validators import MaxValueValidator, MinValueValidator


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    is_paid = models.BooleanField(default=False)

    f_name = models.CharField(max_length=90)
    l_name = models.CharField(max_length=90)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    address = models.TextField()
    postal_code = models.CharField(max_length=10)

    discount = models.IntegerField(blank=True, null=True, default=None)

    created = models.DateTimeField(auto_now_add=True)

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
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=1)
    color = models.ManyToManyField(Color)
    price_with_discount = models.PositiveIntegerField()

    def __str__(self):
        return self.product.title

    @property
    def get_total_price(self):
        return self.price_with_discount * self.quantity


class Coupon(models.Model):
    code = models.CharField(max_length=12, unique=True)
    discount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(90)])

    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()

    active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.code} - {self.discount}%'
