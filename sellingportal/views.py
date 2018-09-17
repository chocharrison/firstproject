from django.shortcuts import render

from django.http import HttpResponse
from sellingportal import models,forms

# Create your views here.
def Index(request):
    context = {'name':'hussein',
               'age':26,
               'jobs':['eng','dev','lecture']}
    return render(request,'index.html',context)
#    return HttpResponse('welcome to indexpage')

def Student(request):
    stuents = models.Student.objects.all()
    context={
        'stuents':stuents
    }
    return render(request,'students.html',context)
 #   return HttpResponse('welcome to student page')

def Register(request):
    msg=''
    form_data = forms.UserRegistrar(request.POST or None)
    if form_data.is_valid():
        student=models.Student()
        student.first_name=form_data.cleaned_data['first_name']
        student.last_name=form_data.cleaned_data['last_name']
        student.age=form_data.cleaned_data['age']
        student.date_birth=form_data.cleaned_data['date_birth']
        student.save()
        msg='data is saved'
    context={
        'formregister': form_data,
        'msg':msg
    }
    return render(request,'registr.html',context)

def StudentDegree(request,student_id):
    #return HttpResponse('welcome to degree page ur id'+student_id)
    degrees = models.Degree.objects.filter(student_id=student_id)
    context={
        'degrees': degrees
    }
    return render(request,'degree.html',context)