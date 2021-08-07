from django import forms
from .models import Mara

class maraForm(forms.ModelForm):
    class Meta:
        model = Mara
        fields = ['title','writer', 'score', 'content', 'img']