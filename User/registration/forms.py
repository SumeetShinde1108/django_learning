from django import forms
from django.core import validators
class UserForm(forms.Form):
    name=forms.CharField()
    contact=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(label='Confirm_Password',widget=forms.PasswordInput)


    def clean(self):
        cleaned_data=super().clean()
        x=self.cleaned_data['password']
        y=self.cleaned_data['rpassword']
        if x!=y:
            raise forms.ValidationError("Enter correct password")
    


