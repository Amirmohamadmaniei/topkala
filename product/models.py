from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Product(models.Model):
    title = models.CharField(max_length=90)
    title_en = models.CharField(max_length=90)
    description = models.TextField()
    brand = models.CharField(max_length=25)

    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
    sub_category = models.ForeignKey('SubCategory', on_delete=models.CASCADE, related_name='products')
    subset = models.ForeignKey('Subset', on_delete=models.CASCADE, related_name='products')

    price = models.IntegerField(validators=[MinValueValidator(0)])
    # is_discount = models.BooleanField(default=False)
    discount = models.IntegerField(default=None, validators=[MaxValueValidator(90), MinValueValidator(0)])

    color = models.ManyToManyField('Color')
    is_available = models.BooleanField(default=True)

    view = models.ManyToManyField('IP')
    sold = models.IntegerField(default=0)

    slug = models.SlugField(allow_unicode=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def get_price_with_discount(self):
        if self.discount > 0:
            return self.price - ((self.discount * self.price) // 100)
        return self.price

    def get_absolute_url(self):
        return reverse('product:detail', args=(self.pk, self.slug))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(args, **kwargs)


class Category(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='category/', null=True)

    slug = models.SlugField(allow_unicode=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(args, **kwargs)


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_categories')
    title = models.CharField(max_length=20)
    slug = models.SlugField(allow_unicode=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(args, **kwargs)


class Subset(models.Model):
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='subsets')
    title = models.CharField(max_length=20)
    slug = models.SlugField(allow_unicode=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(args, **kwargs)


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product/')

    def __str__(self):
        return self.product.title


class Color(models.Model):
    title = models.CharField(max_length=20)
    title_en = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class SubDescription(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sub_descriptions')
    title = models.CharField(max_length=60)
    description = models.TextField()

    def __str__(self):
        return self.title


class Property(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='properties')
    key = models.CharField(max_length=20)
    value = models.CharField(max_length=70)

    def __str__(self):
        return f'{self.key} : {self.value}'



class IP(models.Model):
    ip = models.GenericIPAddressField()

    def __str__(self):
        return self.ip