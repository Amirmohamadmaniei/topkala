from django import forms
from comment.models import Comment, Question


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('full_name', 'body')
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خود را وارد کنید'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': '5', 'placeholder': 'نظر خود را وارد کنید'})
        }


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('full_name', 'body', 'parent')
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خود را وارد کنید'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': '5', 'placeholder': 'نظر خود را وارد کنید'}),
            'parent': forms.HiddenInput(attrs={'id': 'parent'}),
        }
