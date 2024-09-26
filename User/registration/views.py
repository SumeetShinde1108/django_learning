from django.shortcuts import render
from django.http import HttpResponseRedirect
from registration.forms import UserForm
from registration.models import UserData

def redirect(request):
     return render(request,'success.html')

def get_data(request):
    if request.method=="POST":

        
        fm=UserForm(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            ct=fm.cleaned_data['contact']
            em=fm.cleaned_data['email']
            ps=fm.cleaned_data['password']
            print('name=',nm)
            print('email=',em)
            print('contact=',ct)
            print('password=',ps)
        
            uc=UserData(name=nm,contact=ct,email=em,password=ps)
            uc.save()
            return HttpResponseRedirect('/success/')
    else:
        fm=UserForm()
    return render(request,'form.html',{'form':fm}) 



    
