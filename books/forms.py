from django import forms
from . import models


class book_Form(forms.ModelForm):
    class Meta:
        model = models.books_post
        fields = "__all__"
