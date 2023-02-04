from .models import User
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('phone', 'email', 'card_number', 'birth_day', 'image', 'f_name', 'l_name', 'is_active', 'is_admin',
                  'last_login')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError('رمز عبور یکسان نیست')
        return password1

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text='you can change password <a href="../password/"> this link </a>')

    class Meta:
        model = User
        fields = ('phone', 'email', 'card_number', 'birth_day', 'image', 'f_name', 'l_name', 'is_active', 'is_admin',
                  'last_login')
