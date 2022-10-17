from django.contrib import admin

# Register your models here.
from apps.persona.models import Persona, EstadoSalud

admin.site.register(Persona)
admin.site.register(EstadoSalud)