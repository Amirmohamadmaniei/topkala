from django.shortcuts import render, redirect
from django.views import View
from home.forms import SearchForm
from product.mixins import SortMixin
from product.models import Product


class HomeView(View):
    def get(self, request):
        products_1 = Product.objects.filter(is_available=True, sub_category=2)[0:8]
        products_2 = Product.objects.filter(is_available=True, sub_category=1)[0:8]
        products_3 = Product.objects.filter(is_available=True, sub_category=3)[0:8]
        products_4 = Product.objects.filter(is_available=True, sub_category=4)[0:8]
        products_5 = Product.objects.filter(is_available=True, sub_category=5)[0:8]

        products_special = Product.objects.filter(is_available=True, discount__gte=40)[0:8]

        random_products = Product.objects.filter(is_available=True, discount__gte=5).order_by('?')[0:3]
        return render(request, 'home/home.html',
                      {'products_1': products_1, 'products_2': products_2, 'products_3': products_3,
                       'products_4': products_4, 'products_5': products_5, 'products_special': products_special,
                       'random_products': random_products})


class AmazingView(SortMixin, View):
    def get(self, request):
        object_list = Product.objects.filter(is_available=True, discount__gte=40).order_by(self.sort)

        count_object = object_list.count()
        return render(request, 'home/amazing.html', {'object_list': object_list, 'count_object': count_object})


class SearchListView(SortMixin, View):
    def get(self, request):
        form = SearchForm(request.GET)

        if form.is_valid():
            search = form.cleaned_data['search']
            object_list = Product.objects.filter(title__icontains=search).order_by(self.sort)
            count_object = object_list.count()
            return render(request, 'product/product_list.html',
                          {'object_list': object_list, 'count_object': count_object})
        return redirect('home:home')
