from django import forms
from django.core.exceptions import ValidationError

from apps.programa.models import Programa


class ProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa
        fields = ('nombre', 'tipo_asistencias', 'requisitos', 'fecha_inicio', 'fecha_fin')

    def clean(self):
        datos_validados = super().clean()
        fecha_inicio = datos_validados['fecha_inicio']
        fecha_fin = datos_validados['fecha_fin']
        if fecha_fin and fecha_inicio > fecha_fin:
            raise ValidationError(
                {'fecha_inicio': 'La fecha de inicio no puede ser posterior a la fecha fin'}
            )

        return datos_validados
