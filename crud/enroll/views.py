from django.shortcuts import render, HttpResponseRedirect
from enroll.forms import StudentRegistration
from enroll.models import User
# This function will add new items and show all items
def add_show(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            
            us = User(name=nm, email=em, password=pw)
            us.save()
            fm = StudentRegistration()

    else:
        fm = StudentRegistration()
    stud = User.objects.all()

    return render(request, 'addandshow.html', {'form': fm, 'stu': stud})

# This function will update the user data
def update_data(request, id):
    # Fetch the specific user by their ID
    pi = User.objects.get(pk=id)
    
    if request.method == "POST":
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')  
    else:
        fm = StudentRegistration(instance=pi)
    
    return render(request, 'updatestudent.html', {'form': fm})

# This function will delete the user data
def delete_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
