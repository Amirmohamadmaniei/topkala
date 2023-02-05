from django import forms


class AddCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=0, max_value=9)
