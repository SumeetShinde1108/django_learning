from django.shortcuts import render
from django.http import HttpResponse
from registration.forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponse("Thank you for your message!")
    else:
        form = ContactForm()

    return render(request, 'registration/form.html', {'form': form})

