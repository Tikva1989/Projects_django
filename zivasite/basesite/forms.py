from django import forms
from django.forms import ModelForm
from .models import ContactDetail

# Create the form class.


class ContactDetailForm(ModelForm):
    class Meta:
        model = ContactDetail
        fields = ['name', 'email']


class ReachOutForm(forms.Form):
    name = forms.CharField(label="שם מלא", max_length=250, required=True, widget=forms.TextInput)
    email = forms.EmailField(label="מייל", widget=forms.EmailField.widget, required=True)

