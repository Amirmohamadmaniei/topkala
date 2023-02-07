from datetime import datetime, timedelta
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from cart.cart import Cart
from order.forms import CheckoutForm, CouponForm
from order.models import OrderItem, Order, Coupon
from product.models import Color


class OrderCreateView(LoginRequiredMixin, View):
    login_url = 'account:login'

    form_class = CheckoutForm
    template_name = 'order/checkout.html'

    def get(self, request):
        if request.user.orders.all():
            request.user.orders.all().delete()
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()

            cart = Cart(request)

            for item in cart:
                order_item = OrderItem.objects.create(order=order, product=item['product'],
                                                      quantity=int(item['quantity']),
                                                      price_with_discount=int(item['price']))
                order_item.color.add(Color.objects.get(title=item['color']))

            cart.clear()

            return redirect('order:detail', order.id)
        return render(request, self.template_name, {'form': self.form_class})


class OrderDetailView(LoginRequiredMixin, View):
    login_url = 'account:login'

    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        items = OrderItem.objects.filter(order=order)

        t1, t2 = datetime.now() + timedelta(days=3), datetime.now() + timedelta(days=8)

        return render(request, 'order/detail_order.html', {'order': order, 'items': items,
                                                           't1': t1, 't2': t2})


class OrderSelectPayment(LoginRequiredMixin, View):
    login_url = 'account:login'
    form_class = CouponForm
    template_name = 'order/shopping_payment.html'

    def setup(self, request, *args, **kwargs):
        self.order = get_object_or_404(Order, id=kwargs['order_id'])
        self.items = OrderItem.objects.filter(order=self.order)

        return super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'order': self.order, 'items': self.items,
                                                    'form_coupon': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            now = datetime.now()
            code = form.cleaned_data['code']
            try:
                coupon = Coupon.objects.get(code__exact=code, valid_from__lte=now, valid_to__gte=now, active=True)
                self.order.discount = coupon.discount
                self.order.save()
            except Coupon.DoesNotExist:
                form.add_error('code', 'کد تخفیف اشتباه است یا منقضی شده است')

        return render(request, self.template_name, {'order': self.order, 'items': self.items,
                                                    'form_coupon': form})
