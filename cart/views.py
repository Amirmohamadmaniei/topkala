from django.shortcuts import render, redirect
from django.views import View
from .cart import Cart
from product.models import Product
from .forms import AddCartForm


class CartDetailView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.session['cart']:
            return redirect('cart:cart_empty')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        cart = Cart(request)
        return render(request, 'cart/cart.html', {'cart': cart, 'cart_total_price': cart.get_total_price(),
                                                  'get_total_price_with_post': cart.get_total_price_with_post})


class CartDetailEmptyView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.session['cart']:
            return redirect('cart:cart')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, 'cart/cart_empty.html')


class CartAdd(View):
    def post(self, request, pk):
        form = AddCartForm(request.POST)
        product = Product.objects.get(pk=pk)
        if form.is_valid():
            cd = form.cleaned_data
            quantity = cd['quantity']
            color = request.POST.get('color')
            cart = Cart(request)
            cart.add(product, quantity, color)
            return redirect('cart:cart')
        return redirect('product:detail', pk, product.slug)


class CartRemove(View):
    def get(self, request, unique_id):
        cart = Cart(request)
        cart.remove(unique_id)
        return redirect('cart:cart')
