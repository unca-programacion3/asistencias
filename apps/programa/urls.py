from django.urls import path

from apps.programa.views import lista_programas

app_name = 'programa'

urlpatterns = [
    path('lista/', lista_programas, name='programa_lista')
]
