from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse('Home page')

def learn_django(request):
    cname='Django'
    duration= '4 Months'
    seats=10
    django_details={'nm':cname,'du':duration,'st':seats }
    return render(request,'courseone.html',django_details)

def learn_python(request):
    return render(request,'coursetwo.html')

def learn_variable(request):
    a="<h1>Hello Variable</h1>"
    return HttpResponse(a)

def learn_math(request):
    a=10+12
    return HttpResponse(a)

def learn_format(request):
    a='Sumeet Shinde'
    return HttpResponse(f'Hello! How are you {a}')

def learn_temp(request):
    return HttpResponse
