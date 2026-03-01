from django import forms 
from . import models

class EstatePost(forms.ModelForm):
    class Meta:
        model = models.EstatePost
        fields = ['apartment', 'images', 'description', 'location', 'fees', 'total_package']