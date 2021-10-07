from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from apps.programa.forms import ProgramaForm
from apps.programa.models import Programa, TipoAsistencia


def lista_programas(request):
    return render(request, 'programa/lista.html',
                  {'programas': Programa.objects.all()})


@csrf_exempt
def creacion_programa_sin_form(request):

    if request.method == 'POST':
        nuevo_programa = Programa()
        nuevo_programa.nombre = request.POST.get('nombre', None)
        nuevo_programa.fecha_inicio = request.POST.get('fecha_inicio', None)
        nuevo_programa.fecha_fin = request.POST.get('fecha_fin') if request.POST.get('fecha_fin') else None

        try:
            nuevo_programa.save()
            messages.success(request,
                             'Se ha agregado correctamente el Programa {}'.format(nuevo_programa))
        except Exception as e:
            messages.error(request, 'No se pude agregar el Programa. {}'.format(e))

        return redirect(reverse('programa:programa_lista'))

    return render(request, 'programa/form_programa.html',
                  {'tipos_asistencias': TipoAsistencia.objects.all()})


def creacion_programa(request):
    if request.method == 'POST':
        programa_form = ProgramaForm(request.POST, request.FILES)
        if programa_form.is_valid():
            nuevo_programa = programa_form.save(commit=True)
            messages.success(request,
                             'Se ha agregado correctamente el Programa {}'.format(nuevo_programa))
            return redirect(reverse('programa:programa_lista'))
    else:
        programa_form = ProgramaForm()

    return render(request, 'programa/programa_form.html', {'form': programa_form})


def edicion_programa(request, programa_id):
    programa = get_object_or_404(Programa, id=programa_id)

    if request.method == 'POST':
        programa_form = ProgramaForm(request.POST, request.FILES, instance=programa)
        if programa_form.is_valid():
            programa_form.save(commit=True)
            messages.success(request,
                             'Se ha editado correctamente el Programa {}'.format(programa))
            return redirect(reverse('programa:programa_lista'))
    else:
        programa_form = ProgramaForm(instance=programa)

    return render(request, 'programa/programa_form.html', {'form': programa_form})
