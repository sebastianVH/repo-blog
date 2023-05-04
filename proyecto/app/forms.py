from django import forms
from .models import *

class PerroForm(forms.ModelForm):
    class Meta:
        model = Perro
        fields= ['nombre', 'raza', 'edad']

class GatoForm(forms.ModelForm):
    class Meta:
        model = Gato
        fields= ['nombre', 'color', 'edad']

class PajaroForm(forms.ModelForm):
    class Meta:
        model = Pajaro
        fields= ['nombre', 'color', 'peso']        