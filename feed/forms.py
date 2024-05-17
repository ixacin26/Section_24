from django import forms
from django.utils import timezone

class PostForm(forms.Form):
    image = forms.FileField()
    text = forms.CharField(label="Description")
