from django import forms


class AddCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=0, max_value=9,
                                  widget=forms.NumberInput(attrs={'class': 'form-control col col-3', }))
