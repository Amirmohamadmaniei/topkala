from django.shortcuts import redirect, get_object_or_404
from django.views import View
from comment.forms import CommentForm, QuestionForm
from comment.models import Question
from product.models import Product


class CommentAddView(View):

    def post(self, request, product_id):
        form = CommentForm(request.POST)
        product = get_object_or_404(Product, id=product_id)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.product = product
            instance.save()

        return redirect('product:detail', product_id, product.slug)


class QuestionView(View):
    def post(self, request, product_id):
        form = QuestionForm(request.POST)
        product = get_object_or_404(Product, id=product_id)
        if form.is_valid():
            parent = request.POST['parent']
            instance = form.save(commit=False)
            instance.product = product
            if parent:
                parent = get_object_or_404(Question, id=parent)
                instance.parent.id = parent
                instance.has_parent = True
            instance.save()

        return redirect('product:detail', product_id, product.slug)
