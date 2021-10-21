from django import forms


class ReachOutForm(forms.Form):
    name = forms.CharField(label="שם מלא", max_length=250, required=True, widget=forms.TextInput)
    email = forms.EmailField(label="מייל", widget=forms.EmailField.widget, required=True)
