from django import forms
from django.core import validators
from registration.models import UserData
class UserForm(forms.Form):

    name=forms.CharField()
    contact=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(label='Confirm_Password',widget=forms.PasswordInput)
    
    '''class meta:
        model=UserData
        fields=['name','contact','email','password','rpassword']
        Labels={'rpassword':'Confirm Password'}
        widgets={'password':forms.PasswordInput,'rpassword':forms.PasswordInput}
        error_messages={'password':"This field can't be empty"}'''

    def clean(self):
        cleaned_data=super().clean()
        x=self.cleaned_data['password']
        y=self.cleaned_data['rpassword']
        if x!=y:
            raise forms.ValidationError("Enter correct password")
    


