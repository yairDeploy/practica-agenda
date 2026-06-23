from django.shortcuts import get_object_or_404, render, redirect
from agenda.forms.telefonoFormSet import TelefonoFormSet
from agenda.models import Contacto


def editar_telefonos(request, contacto_id):
    contacto = get_object_or_404(Contacto, id=contacto_id)

    if request.method == 'POST':
        print("POST data:", request.POST)  # Debugging line to print POST data
        formset = TelefonoFormSet(request.POST, instance=contacto)
        print("Formset is valid:", formset.is_valid())
        if formset.is_valid():
            formset.save()
            return redirect('editar_telefonos', contacto_id=contacto.id)
    else:
        formset = TelefonoFormSet(instance=contacto)

    return redirect('editar_contacto', id=contacto.id, tab='telefono')