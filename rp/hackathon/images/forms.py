from dataclasses import field
from pyexpat import model
from django import forms
from .models import Image

class AddImageForm(forms.Form):
    imageName = forms.CharField()
    imageUrl = forms.ImageField()
    imageDetails = forms.CharField()