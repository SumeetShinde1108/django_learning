from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

# SignUp View
def sign_up(request):
    if request.method=="POST":
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Account Created Successfully') 
    else:
        fm=SignUpForm()
    return render (request,'signup.html',{'form':fm})            
# LogIn View
def  user_login(request):
    if request.method=="POST":
        fm=AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request, user)
                messages.success(request,'Logged in successfully..!')
                return HttpResponseRedirect('/profile/')
    else:
        fm=AuthenticationForm() 
    return render (request,'userlogin.html',{'form':fm})
 
# Profile
def user_profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html',{'name':request.name})
    else:
        return HttpResponseRedirect('/login/')

#Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/logout/')


    