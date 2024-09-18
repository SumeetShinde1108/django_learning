from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime 
from .models import Student
def index(request):
    return render(request,'Home.html')

def learn_django(request):
    date_time=datetime.now()
    cname='Django'
    duration= '4 Months'
    seats='5'
    title='Learn Django'
    django_details={'tt':title, 'nm':cname,'du':duration,'st':seats ,'dt':date_time}
    return render(request,'django.html',django_details)

def studentinfo(request):
    stud=Student.objects.all()
    return render(request,'student.html',{'st':stud})

def learn_python(request):
    cname='Python'
    py_details={'cn':cname}
    return render(request,'python.html',py_details)

def learn_variable(request):
    a="Hello! This is a variable page"
    var_details={'var':a}
    return render(request,'variable.html',var_details)

def about(request):
    return HttpResponse("THIS ABOUT PAGE")    


