from django import forms
from django.forms import DateInput

from apps.persona.models import Persona, EstadoSalud


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('dni', 'nombre_completo', 'fecha_nacimiento', 'sexo', 'domicilio')

        widgets = {
            'fecha_nacimiento': DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }


class EstadoSaludForm(forms.ModelForm):
    class Meta:
        model = EstadoSalud
        fields = ('es_discapacitado', 'posee_obesidad', 'posee_desnutricion', 'observaciones')
