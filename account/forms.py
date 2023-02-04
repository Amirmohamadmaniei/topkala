from django import forms
from .models import User
from django.core.exceptions import ValidationError


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-field',
                                                             'placeholder': 'ایمیل یا شماره موبایل خود را وارد نمایید'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-field',
                                                                 'placeholder': 'رمز عبور خود را وارد نمایید'}))


class UserRegisterForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-field',
                                                          'placeholder': 'شماره موبایل خود را وارد نمایید'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-field',
                                                                 'placeholder': 'رمز عبور خود را وارد نمایید'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-field',
                                                                  'placeholder': 'رمز عبور خود را تایید کنید'}))

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit():
            raise ValidationError('شماره تلفن باید عددی باشد')

        if len(phone) != 11:
            raise ValidationError('شماره تلفن باید ۱۱ رقمی باشد')

        if not phone.startswith('09'):
            raise ValidationError('شماره تلفن باید با 09 شروع شود')

        user = User.objects.filter(phone=phone).exists()
        if user:
            raise ValidationError('شماره تلفن قبلا ثبت شده است')
        return phone

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not 128 > len(password) >= 8:
            raise ValidationError('رمز عبور باشد بیشتر از ۸ رقم باشد')
        return password

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise ValidationError('رمز عبور یکسان نیست')
        return password


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input-field', 'placeholder': 'رمز عبور قبلی خود را وارد نمایید'}))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input-field', 'placeholder': 'رمز عبور جدید خود را وارد نمایید'}))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input-field', 'placeholder': 'رمز عبور جدید خود را مجددا وارد نمایید'}))

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not 128 > len(password) >= 8:
            raise ValidationError('رمز عبور باشد بیشتر از ۸ رقم باشد')
        return password

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise ValidationError('رمز عبور یکسان نیست')
        return password
