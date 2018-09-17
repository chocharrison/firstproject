from django import forms
from django.forms import ModelForm
from firstapp.models import Register
class RegistrationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=10)
    email=forms.EmailField()
    
    class Meta:
        model = Register
        fields = ('first_name','last_name','email',)
        
