from dataclasses import fields
from socket import fromshare
from django import forms
from .models import *

class PersonalForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PersonalForm, self).__init__(*args, **kwargs)
        self.fields['area'].empty_label = 'Selecciona'
        self.fields['estudios'].empty_label = 'Selecciona'
        self.fields['carrera'].empty_label = 'Selecciona'
        self.fields['carrera'].choices = [('', 'Selecciona'),] + list(self.fields['carrera'].choices)[1:]
        self.fields['apellido_paterno'].required = True
        self.fields['apellido_materno'].required = True
