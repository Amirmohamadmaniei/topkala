from django.shortcuts import render
from django.views import View
from order.models import OrderItem, Order
from product.models import Product, Color


class OrderInformationView(View):
    def get(self, request):
        cart = request.session.get('cart')
        # Order.objects.create(user=request.user)

        for item in cart.values():
            product = Product.objects.get(id=int(item['id']))
            order_item = OrderItem.objects.create(product=product, quantity=int(item['quantity']),
                                     price_with_discount=int(item['price']))
            color = Color.objects.get(title=item['color'])

            order_item.color.add(color)

        return render(request, 'order/shopping.html', {})
