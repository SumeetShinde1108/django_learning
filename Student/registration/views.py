from django.shortcuts import render
from django.http import HttpResponseRedirect
from registration.forms import ContactForm

def output(request):
    return render(request,'output.html')
def contact_view(request):
    if request.method=="POST":
        fm=ContactForm(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            email=fm.cleaned_data['email']
            address=fm.cleaned_data['address']
            print("Form is validated")
            print('name:',name)
            print('email:',email)
            print('address:',address)
            details={'nm':name,'em':email,'add':address}
            return HttpResponseRedirect('/success/')
            #return render(request,'output.html',details)
    else:
        fm=ContactForm() 
        print("This coming from get request")
    return render(request, 'form.html', {'form': fm})

