from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm
from .models import Register
# Create your views here.
def index(request):
   # return HttpResponse("<H2> hi</H2>")
   form = RegistrationForm()
   if form.is_valid():
      first_name= form.cleaned_data['first_name']
      last_name= form.cleaned_data['last_name']
      email= form.cleaned_data['email']
      f = Register(first_name=first_name,last_name=last_name,email=email)
      f.save()
   return render(request,"firstapp/index.html",{
       "myregistrationform": form
   })