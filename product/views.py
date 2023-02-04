from django.shortcuts import render
from django.views import View
from .models import Product


class ProductDetail(View):
    def get(self, request, pk, slug):
        product = Product.objects.get(pk=pk, slug=slug)
        return render(request, 'product/product_detail.html', {'object': product})
