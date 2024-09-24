from django.shortcuts import render
from django.http import HttpResponse
from registration.forms import ContactForm

def contact_view(request):
    form = ContactForm(auto_id=True,initial={'name':'Sumeet','email':'sumeet@123.com'},)
    form.order_fields(field_order=['address','email','name']) #ordering fields 
    return render(request, 'registration/form.html', {'form': form})

