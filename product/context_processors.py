from home.forms import SearchForm
from .models import Category
from cart.cart import Cart


def category(request):
    form_search = SearchForm()
    cart = Cart(request)
    return {'categories': Category.objects.all(), 'cart': cart,
            'form_search': form_search}
