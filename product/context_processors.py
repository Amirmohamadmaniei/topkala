from .models import Category
from cart.cart import Cart


def category(request):
    cart = Cart(request)
    return {'categories': Category.objects.all(), 'cart': cart}
