from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Product(models.Model):
    title = models.CharField(max_length=90, verbose_name='عنوان')
    title_en = models.CharField(max_length=90, verbose_name='عنوان انگلیسی')
    description = models.TextField(verbose_name='توضیحات')
    brand = models.CharField(max_length=25, verbose_name='برند')

    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products',
                                 verbose_name='دسته بندی کلی')
    sub_category = models.ForeignKey('SubCategory', on_delete=models.CASCADE, related_name='products',
                                     verbose_name='زیر دسته بندی')
    subset = models.ForeignKey('Subset', on_delete=models.CASCADE, related_name='products', verbose_name='زیر مجموعه')

    price = models.IntegerField(validators=[MinValueValidator(0)], verbose_name='قیمت')
    discount = models.IntegerField(default=None, validators=[MaxValueValidator(90), MinValueValidator(0)],
                                   verbose_name='تخفیف')

    color = models.ManyToManyField('Color', verbose_name='رنگ')
    is_available = models.BooleanField(default=True, verbose_name='موجود')

    view = models.ManyToManyField('IP', blank=True, verbose_name='بازذیذ')
    sold = models.IntegerField(default=0, verbose_name='تعداد فروش')

    slug = models.SlugField(allow_unicode=True, blank=True, verbose_name='اسلاگ')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

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
    title = models.CharField(max_length=20, verbose_name='عنوان')
    image = models.ImageField(upload_to='category/', null=True, verbose_name='عکس')

    slug = models.SlugField(allow_unicode=True, blank=True, verbose_name='اسلاگ')

    class Meta:
        verbose_name = 'دسته بندی کلی'
        verbose_name_plural = 'دسته بندی های کلی'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(args, **kwargs)


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_categories',
                                 verbose_name='دسته بندی')
    title = models.CharField(max_length=20, verbose_name='عنوان')
    slug = models.SlugField(allow_unicode=True, blank=True, verbose_name='اسلاگ')

    class Meta:
        verbose_name = 'زیر دسته بندی'
        verbose_name_plural = 'زیر دسته بندی ها'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(args, **kwargs)


class Subset(models.Model):
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='subsets',
                                 verbose_name='دسته بندی')
    title = models.CharField(max_length=20, verbose_name='عنوان')
    slug = models.SlugField(allow_unicode=True, blank=True, verbose_name='اسلاگ')

    class Meta:
        verbose_name = 'زیر مجموعه'
        verbose_name_plural = 'زیر مجموعه ها'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(args, **kwargs)


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name='محصول')
    image = models.ImageField(upload_to='product/', verbose_name='عکس')

    class Meta:
        verbose_name = 'عکس'
        verbose_name_plural = 'عکس ها'

    def __str__(self):
        return self.product.title


class Color(models.Model):
    title = models.CharField(max_length=20, verbose_name='عنوان رنگ')

    class Meta:
        verbose_name = 'رنگ'
        verbose_name_plural = 'رنگ ها'

    def __str__(self):
        return self.title


class SubDescription(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sub_descriptions',
                                verbose_name='محصول')
    title = models.CharField(max_length=60, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')

    class Meta:
        verbose_name = 'توضیح'
        verbose_name_plural = 'توضیحات'

    def __str__(self):
        return self.title


class Property(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='properties', verbose_name='محصول')
    key = models.CharField(max_length=20, verbose_name='ویژگی')
    value = models.CharField(max_length=70, verbose_name='مقدار ویژگی')

    class Meta:
        verbose_name = 'ویژگی'
        verbose_name_plural = 'ویژگی ها'

    def __str__(self):
        return f'{self.key} : {self.value}'


class IP(models.Model):
    ip = models.GenericIPAddressField(verbose_name='ip')

    class Meta:
        verbose_name = 'IP'
        verbose_name_plural = 'IPs'

    def __str__(self):
        return self.ip
