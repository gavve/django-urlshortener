__author__ = 'jacob'
from django import forms
from .models import Url

class UrlForm(forms.ModelForm):
    class Meta:
        model = Url
        exclude = ['short_url', 'word']