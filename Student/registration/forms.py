from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(error_messages={'required':'Enter Your Name'})
    email = forms.EmailField(initial='e.g. sumeet@123.com')
    address=forms.CharField(help_text="In this field we can write 30 letters")
 