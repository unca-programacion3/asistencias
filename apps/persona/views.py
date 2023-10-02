from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from apps.persona.forms import PersonaForm, EstadoSaludForm
from apps.persona.models import Persona


def persona_lista(request):
    personas = Persona.objects.all().select_related('estadosalud')
    return render(request, 'persona/lista.html',
                  {'personas': personas})


def persona_detalle(request, pk):
    persona = get_object_or_404(Persona.objects.select_related('estadosalud'), pk=pk)
    return render(request,
                  'persona/detalle.html',
                  {'persona': persona})


def persona_create(request):
    if request.method == 'POST':
        # En PersonaForm se guardan los datos que provienen con el prefijo "persona". Lo mismo pasa con el form estado salud
        # https://docs.djangoproject.com/en/4.1/ref/forms/api/#prefixes-for-forms

        form_persona = PersonaForm(request.POST, prefix='persona')
        form_estado_salud = EstadoSaludForm(request.POST, prefix='estado_salud')

        if form_persona.is_valid() and form_estado_salud.is_valid():
            persona_instance = form_persona.save()

            estado_salud_instance = form_estado_salud.save(commit=False)
            # asignar persona a estado salud
            estado_salud_instance.persona = persona_instance
            estado_salud_instance.save()

            messages.success(request, 'Se ha agregado la persona correctamente.')
            return redirect(reverse('persona:persona_detalle', args={persona_instance.id}))

    else:
        form_persona = PersonaForm(prefix='persona')
        form_estado_salud = EstadoSaludForm(prefix='estado_salud')

    return render(request, 'persona/persona_form.html', {
        'form_persona': form_persona,
        'form_estado_salud': form_estado_salud
    })
