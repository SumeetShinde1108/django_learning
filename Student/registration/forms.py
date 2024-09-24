from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    address=forms.CharField(help_text="In this field we can write 30 characters")
