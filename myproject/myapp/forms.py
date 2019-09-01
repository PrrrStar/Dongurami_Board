from django import forms
from myapp.models import boardConf

class boardForm(forms.ModelForm):
 
    class Meta:
        model = boardConf
        fields = ('title','writer','text')