from django.shortcuts import render

from apps.programa.models import Programa


def lista_programas(request):
    return render(request, 'programa/lista.html',
                  {'programas': Programa.objects.all()})
