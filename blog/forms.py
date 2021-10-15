from django import forms
from django.db.models import fields
from .models import posts,comments



class postFrom(forms.ModelForm):
    class Meta:
        model = posts
        fields = '__all__'



class commentForm(forms.ModelForm):
    class Meta:
        model = comments
        fields = ['text',]