from django import forms 
from . import models

class EstatePost(forms.ModelForm):
    class Meta:
        model = models.EstatePost
        fields = ['title', 'images','details','location','price', 'house_type', 'bedroom', 'bathroom', 'toilet']