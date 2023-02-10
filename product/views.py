from django.shortcuts import render, get_object_or_404
from django.views import View
from comment.forms import CommentForm, QuestionForm
from comment.models import Comment, Question
from profiles.models import Favorite
from .mixins import SortMixin
from .models import Product, Category, SubCategory, Subset
from cart.forms import AddCartForm
from django.core.paginator import Paginator


class ProductDetailView(View):
    def get(self, request, pk, slug):
        form = AddCartForm()
        form_comment = CommentForm()
        form_question = QuestionForm()

        product = get_object_or_404(Product, id=pk, slug=slug)
        properties = product.properties.all()

        comments = Comment.objects.filter(product=product)
        questions = Question.objects.filter(product=product, has_parent=False)

        if request.user.is_authenticated:
            is_favorite = Favorite.objects.filter(user=request.user, product=product).exists()
        else:
            is_favorite = False

        if not request.user.ip_address in product.view.all():
            product.view.add(request.user.ip_address)

        return render(request, 'product/product_detail.html',
                      {'object': product, 'form': form, 'is_favorite': is_favorite, 'comments': comments,
                       'questions': questions, 'primary_property': properties, 'secondary_property': properties[0:5],
                       'form_comment': form_comment, 'form_question': form_question})


class ProductListCategoryView(SortMixin, View):
    def get(self, request, category_slug):
        category = get_object_or_404(Category, slug=category_slug)

        object_list = Product.objects.filter(category=category).order_by(self.sort)

        paginator = Paginator(object_list, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        count_object = object_list.count()

        return render(request, 'product/product_list.html', {'object_list': page_obj, 'count_object': count_object})


class ProductListSubCategoryView(SortMixin, View):
    def get(self, request, category_slug, sub_category_slug):
        category = get_object_or_404(Category, slug=category_slug)
        sub_category = get_object_or_404(SubCategory, slug=sub_category_slug)
        object_list = Product.objects.filter(category=category, sub_category=sub_category).order_by(self.sort)

        paginator = Paginator(object_list, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        count_object = object_list.count()

        return render(request, 'product/product_list.html', {'object_list': page_obj, 'count_object': count_object})


class ProductListSubsetView(SortMixin, View):
    def get(self, request, category_slug, sub_category_slug, subset_slug):
        category = get_object_or_404(Category, slug=category_slug)
        sub_category = get_object_or_404(SubCategory, slug=sub_category_slug)
        subset = get_object_or_404(Subset, slug=subset_slug)

        object_list = Product.objects.filter(category=category, sub_category=sub_category, subset=subset).order_by(
            self.sort)

        paginator = Paginator(object_list, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        count_object = object_list.count()

        return render(request, 'product/product_list.html', {'object_list': page_obj, 'count_object': count_object})
