from django.urls import path

from apps.programa.views import lista_programas, creacion_programa_sin_form, creacion_programa, edicion_programa

app_name = 'programa'

urlpatterns = [
    path('lista/', lista_programas, name='programa_lista'),
    path('crear/', creacion_programa_sin_form, name='programa_creacion_sin_form'),
    path('creacion/', creacion_programa, name='programa_creacion'),
    path('edicion/<int:programa_id>', edicion_programa, name='programa_edicion')
]
