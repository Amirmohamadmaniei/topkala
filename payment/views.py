from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404, render
from django.views import View
from django.contrib import messages
from order.models import Order
import requests
import json

MERCHANT = ''
ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"
CallbackURL = 'http://127.0.0.1:8000/payment/verify/'


class SendRequestView(LoginRequiredMixin, View):
    login_url = 'account:login'

    def get(self, request, order_id):

        order = get_object_or_404(Order, id=order_id)
        phone = request.user.phone
        email = request.user.email
        description = "خرید از سایت تاپ کالا"
        request.session['order_id'] = order_id

        req_data = {
            "merchant_id": MERCHANT,
            "amount": int(str(order.get_total_price) + '0'),
            "callback_url": CallbackURL,
            "description": description,
            "metadata": {"mobile": str(phone), "email": email}
        }
        req_header = {"accept": "application/json", "content-type": "application/json'"}
        req = requests.post(url=ZP_API_REQUEST, data=json.dumps(req_data), headers=req_header)
        print(req.json()['data']['authority'])
        authority = req.json()['data']['authority']
        if len(req.json()['errors']) == 0:
            return redirect(ZP_API_STARTPAY.format(authority=authority))
        else:
            e_code = req.json()['errors']['code']
            e_message = req.json()['errors']['message']
            return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")


class VerifyView(LoginRequiredMixin, View):
    login_url = 'account:login'

    def get(self, request):
        order_id = request.session.get('order_id')
        order = get_object_or_404(Order, id=order_id)
        del request.session['order_id']

        t_status = request.GET.get('Status')
        t_authority = request.GET['Authority']
        if request.GET.get('Status') == 'OK':
            req_header = {"accept": "application/json",
                          "content-type": "application/json'"}
            req_data = {
                "merchant_id": MERCHANT,
                "amount": int(str(order.get_total_price) + '0'),
                "authority": t_authority
            }
            req = requests.post(url=ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
            if len(req.json()['errors']) == 0:
                t_status = req.json()['data']['code']
                if t_status == 100:

                    order.is_paid = True
                    order.save()
                    ref_id = str(req.json()['data']['ref_id'])

                    for item in order.items.all():
                        item.product.sold += 1

                    messages.success(request, 'خرید با موفقیت انجام شد', extra_tags='alert alert-success')
                    return render(request, 'payment/shopping_complete.html', {'ref_id': ref_id, 'order': order,
                                                                              'message': 'خرید با موفقیت انجام شد'})

                elif t_status == 101:

                    messages.warning(request, 'خرید قبلا ثبت شده است', extra_tags='alert alert-warning')
                    return render(request, 'payment/shopping_not_complete.html',
                                  {'message': 'خرید شما قبلا ثبت شده است'})

                else:
                    messages.error(request, 'خرید موفقیت آمیز نبود', extra_tags='alert alert-danger')
                    return render(request, 'payment/shopping_not_complete.html', {'message': ''})

            else:

                messages.error(request, 'خرید موفقیت آمیز نبود', extra_tags='alert alert-danger')
                return render(request, 'payment/shopping_not_complete.html', {'message': ''})

        else:

            messages.error(request, 'خرید توسط کاربر لغو شد', extra_tags='alert alert-danger')
            return render(request, 'payment/shopping_not_complete.html', {'message': ''})
