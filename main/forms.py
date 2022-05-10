from django import forms

from .models import Comment, Emails


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class EmailsForm(forms.ModelForm):

    """Класс для формы ввода электронного адреса"""

    email = forms.EmailField(required=True, label='Электронный адрес')

    class Meta:
        model = Emails
        fields = ['email']



