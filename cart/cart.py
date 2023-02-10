from django.shortcuts import get_object_or_404
from home.models import Post
from product.models import Product

CART_SESSION_ID = 'cart'


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        cart = self.cart.copy()

        for item in cart.values():
            item['product'] = get_object_or_404(Product, id=int(item['id']))
            item['total'] = int(item['quantity']) * int(item['product'].get_price_with_discount)
            item['unique_id'] = self.unique_id_generate(item['id'], item['color'])
            yield item

    def add(self, product, quantity, color):
        unique = self.unique_id_generate(product.id, color)
        if unique not in self.cart:
            self.cart[unique] = {'id': str(product.id), 'quantity': 0, 'color': color,
                                 'price': str(product.get_price_with_discount)}
        self.cart[unique]['quantity'] += quantity
        self.save()

    def remove(self, unique_id):
        if unique_id in self.cart:
            del self.cart[unique_id]
            self.save()

    def unique_id_generate(self, id, color):
        return f'{id}-{color}'

    def get_total_price(self):
        return sum(int(item['price']) * int(item['quantity']) for item in self.cart.values())

    def get_total_price_with_post(self):
        post_cost = Post.objects.all().last()
        return sum(int(item['price']) * int(item['quantity']) for item in self.cart.values()) + post_cost.cost

    def get_count_item(self):
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[CART_SESSION_ID]
        self.save()

    def save(self):
        self.session.modified = True
