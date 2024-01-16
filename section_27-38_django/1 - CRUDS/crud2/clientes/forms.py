from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        # fields = '__all__'
        fields = ('nombre', 'apellido_paterno', 'apellido_materno', 'foto', 'lenguaje', 'sistema_operativo')
        labels = {'nombre': 'Proporciona tu nombre:', 'apellido_paterno': 'Proporciona tu primer apellido:'}

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.fields['lenguaje'].empty_label = 'Selecciona el Lenguaje'
        self.fields['sistema_operativo'].empty_label = 'Selecciona un sistema operativo'
        self.fields['apellido_materno'].required = False