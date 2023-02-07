from django import forms
from order.models import Order


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('f_name', 'l_name', 'email', 'phone', 'address', 'postal_code')
        widgets = {
            'f_name': forms.TextInput(attrs={'class': 'input-field text-right', 'placeholder': 'نام خود را وارد کنید'}),
            'l_name': forms.TextInput(attrs={'class': 'input-field text-right', 'placeholder': 'نام خانوادگی خود را وارد کنید'}),
            'email': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'ایمیل خود را وارد کنید'}),
            'phone': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'شماره موبایل خود را وارد نمایید'}),
            'address': forms.Textarea(attrs={'class': 'input-field text-right', 'placeholder': 'آدرس پستی خود را وارد کنید'}),
            'postal_code': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'کد پستی خود را وارد کنید'}),
        }


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={'class': 'ui-input-field', 'placeholder': 'مثلا 837A2CS'}))
