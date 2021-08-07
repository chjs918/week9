from django import forms
from .models import Usercontact

class UsercontactForm(forms.ModelForm):
    class Meta: 
        model = Usercontact
        fields = ['title', 'toID', 'fromID', 'content']