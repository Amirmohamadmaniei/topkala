from django.shortcuts import render, get_object_or_404
from django.views import View
from profiles.models import Favorite
from .models import Product, Category, SubCategory, Subset
from cart.forms import AddCartForm


class ProductDetailView(View):
    def get(self, request, pk, slug):
        form = AddCartForm()
        product = Product.objects.get(pk=pk, slug=slug)
        properties = product.properties.all()
        if request.user.is_authenticated:
            is_favorite = Favorite.objects.filter(user=request.user, product=product).exists()
        else:
            is_favorite = False
        return render(request, 'product/product_detail.html', {'object': product, 'form': form,
                                                               'is_favorite': is_favorite,
                                                               'primary_property': properties,
                                                               'secondary_property': properties[0:5]})


class ProductListView(View):
    def get(self, request):
        object_list = Product.objects.all()
        return render(request, 'product/product_list.html', {'object_list': object_list})


class ProductListCategoryView(View):
    def get(self, request, category_slug):
        category = get_object_or_404(Category, slug=category_slug)
        object_list = Product.objects.filter(category=category)
        return render(request, 'product/product_list.html', {'object_list': object_list})


class ProductListSubCategoryView(View):
    def get(self, request, category_slug, sub_category_slug):
        sub_category = get_object_or_404(SubCategory, slug=sub_category_slug)
        category = get_object_or_404(Category, slug=category_slug)
        object_list = Product.objects.filter(category=category, sub_category=sub_category)
        return render(request, 'product/product_list.html', {'object_list': object_list})


class ProductListSubsetView(View):
    def get(self, request, category_slug, sub_category_slug, subset_slug):
        subset = get_object_or_404(Subset, slug=subset_slug)
        sub_category = get_object_or_404(SubCategory, slug=sub_category_slug)
        category = get_object_or_404(Category, slug=category_slug)
        object_list = Product.objects.filter(category=category, sub_category=sub_category, subset=subset)
        return render(request, 'product/product_list.html', {'object_list': object_list})
