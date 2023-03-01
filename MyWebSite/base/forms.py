from django import forms
from .models import Contact
from phonenumber_field.formfields import PhoneNumberField

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First Name'
    }))
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Last Name'
    }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'E-Mail'
    }))
    phone = PhoneNumberField(required=True, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'type' : 'tel',
        'pattern' : '[0-9]{2}-[0-9]{3}-[0-9]{3}-[0-9]{4}',
        'placeholder': '+90-123-456-7890'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Your Message'
    }))

    class Meta:
        model = Contact
        fields = ['first_name','last_name','email','phone','message']