from django.shortcuts import render
from django.views import View
from product.models import Product


class HomeView(View):
    def get(self, request):
        products = Product.objects.filter(is_available=True, sub_category=1)[0:8]
        return render(request, 'home/home.html', {'products': products})
