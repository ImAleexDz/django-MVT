from unicodedata import name
from django import forms

class PersonForm(forms.Form):
    name = forms.CharField(label="Nombre",max_length=20, required=True)
    lastname = forms.CharField(label="Apellido",max_length=30, required=True)
    phone = forms.CharField(label="Teléfono", required=True)
    birthday = forms.DateField(label="Cumpleaños (YYYY-MM-DD)")
    age = forms.IntegerField(label="Edad")

