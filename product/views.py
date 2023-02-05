from django.shortcuts import render
from django.views import View
from .models import Product
from cart.forms import AddCartForm


class ProductDetail(View):
    def get(self, request, pk, slug):
        product = Product.objects.get(pk=pk, slug=slug)
        form = AddCartForm()
        return render(request, 'product/product_detail.html', {'object': product, 'form': form})
