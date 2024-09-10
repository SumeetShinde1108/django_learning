from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime 
def index(request):
    return HttpResponse('Home page')

def learn_django(request):
    date_time=datetime.now()
    cname='Django'
    duration= '4 Months'
    seats='5'
    title='Learn Django'
    django_details={'tt':title, 'nm':cname,'du':duration,'st':seats ,'dt':date_time}
    return render(request,'courseone.html',django_details)

def learn_python(request):
    cname='Python'
    py_details={'cn':cname}
    return render(request,'coursetwo.html',py_details)

def learn_variable(request):
    a="Hello! This is a variable page"
    var_details={'var':a}
    return render(request,'child.html',var_details)

def learn_math(request):
    a=10+12
    return HttpResponse(a)

def learn_format(request):
    a='Sumeet Shinde'
    return HttpResponse(f'Hello! How are you {a}')

def learn_temp(request):
    return HttpResponse
