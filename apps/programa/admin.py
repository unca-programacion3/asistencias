from django.contrib import admin

# Register your models here.
from apps.programa.models import Programa, TipoAsistencia


@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_inicio', 'fecha_fin')
    search_fields = ('nombre',)
    list_filter = ('tipo_asistencias',)
    date_hierarchy = 'fecha_inicio'
    autocomplete_fields = ('tipo_asistencias', )
    ordering = ('nombre',)


@admin.register(TipoAsistencia)
class TipoAsistenciaAdmin(admin.ModelAdmin):
    search_fields = ('descripcion',)

