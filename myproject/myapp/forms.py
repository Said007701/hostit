from django import forms
from .models import index1, index2

class index2Form(forms.ModelForm):
    class Meta:
        model = index2
        fields = ['home','about', 'service','price', 'contact']

class index1Form(forms.ModelForm):
    class Meta:
        model = index1
        fields = ['title']

