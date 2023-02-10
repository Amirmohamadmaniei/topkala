from django import forms
from account.models import User


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('f_name', 'l_name', 'email', 'birth_day', 'card_number')
        widgets = {
            'f_name': forms.TextInput(
                attrs={'class': 'input-field text-right', 'placeholder': 'نام خود را وارد نمایید'}),
            'l_name': forms.TextInput(
                attrs={'class': 'input-field text-right', 'placeholder': 'نام خانوادگی خود را وارد نمایید'}),
            'email': forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'آدرس ایمیل خود را وارد نمایید'}),
            'birth_day': forms.DateInput(attrs={'class': 'input-field', 'type': 'date'}),
            'card_number': forms.TextInput(
                attrs={'class': 'input-field', 'placeholder': ' شماره کارت خود را وارد نمایید'}),
        }
