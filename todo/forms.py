from django import forms

from .models import ToDo



class TODOForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ["title", "status", "priority"]








