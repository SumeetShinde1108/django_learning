from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(error_messages={'required':'Enter Your Name'})
    email = forms.EmailField(initial='e.g. sumeet@123.com')
    address=forms.CharField(help_text="In this field we can write 30 letters")
    agree=forms.BooleanField(label="I Agree")
    def clean(self):
        cleaned_data=super().clean()
        val = self.cleaned_data['name']
        if len(val)<4:
            raise forms.ValidationError('Enter the name which contains more than 4 characters')     

        valname=self.cleaned_data['email']
        if len(valname)<10:
            raise forms.ValidationError("Enter email address which contains more than 10 characters")
