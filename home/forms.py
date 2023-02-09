from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'جستجو ...'}))
