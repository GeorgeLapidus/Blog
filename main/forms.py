from django import forms

from .models import Comment, Emails, AnswerComment


class CommentForm(forms.ModelForm):
    """Класс формы для ввода комментария """
    class Meta:
        model = Comment
        fields = ['text']

class AnswerCommentForm(forms.ModelForm):
    """Класс формы для ввода ответа на комментарий """
    class Meta:
        model = AnswerComment
        fields = ['text']

class EmailsForm(forms.ModelForm):

    """Класс для формы ввода электронного адреса"""

    email = forms.EmailField(required=True, label='Электронный адрес')

    class Meta:
        model = Emails
        fields = ['email']



