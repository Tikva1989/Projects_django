from django import forms
from .models import Family, Animal, Person, Passport, Country

class AnimalForm(forms.Form):
    name = forms.CharField(max_length=40)
    legs = forms.IntegerField()
    weight = forms.FloatField()
    height = forms.FloatField()
    speed = forms.FloatField()
    family = forms.ModelChoiceField(queryset=Family.objects.all())


class FamilyForm(forms.Form):
    name = forms.CharField(max_length=40)

class PersonForm(forms.Form):
    first_name = forms.CharField(max_length=40) 
    last_name = forms.CharField(max_length=40)
    country_of_origin = forms.ModelChoiceField(queryset=Country.objects.all())


class PassportForm(forms.Form):
    person = forms.ModelChoiceField(queryset=Person.objects.filter(passport=None))
    pass_id = forms.CharField(max_length=10)
    visited_countries = forms.ModelMultipleChoiceField(queryset=Country.objects.all())