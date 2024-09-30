from django.shortcuts import render
from enroll.forms import StudentRegistration
from enroll.models import User
def add_show(request):
    if request.method=="POST":
        fm=StudentRegistration(request.POST)
    else:
        fm=StudentRegistration()

        
    return render(request,'addandshow.html',{'form':fm})

