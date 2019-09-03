from django import forms
from myapp.models import myapp

class boardForm(forms.ModelForm):
 
    class Meta:
        model = myapp
        fields = ('title','writer','text')