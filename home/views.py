from django.shortcuts import render
from django.views import View
from product.models import Product


class HomeView(View):
    def get(self, request):
        products_1 = Product.objects.filter(is_available=True, sub_category=2)[0:8]
        products_2 = Product.objects.filter(is_available=True, sub_category=1)[0:8]
        products_3 = Product.objects.filter(is_available=True, sub_category=3)[0:8]
        products_4 = Product.objects.filter(is_available=True, sub_category=4)[0:8]
        products_5 = Product.objects.filter(is_available=True, sub_category=5)[0:8]

        products_special = Product.objects.filter(is_available=True, discount__gte=40)[0:8]
        return render(request, 'home/home.html',
                      {'products_1': products_1, 'products_2': products_2, 'products_3': products_3,
                       'products_4': products_4, 'products_5': products_5, 'products_special': products_special})
