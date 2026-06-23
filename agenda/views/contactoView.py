from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from agenda.forms.contactoForms import ContactoForm
from agenda.models import Contacto

def inicio(request):
    contactos = Contacto.objects.all()
    context = {
        "titulo": "Inicio",
        "encabezado": "Agenda - Contactos",
        "contactos": contactos
    }
    return render(request, 'index.html', context)

class ContactoView():
    def crear(request):
        contactoForm = ContactoForm()
        render_dict = {
            'form': contactoForm,
            'encabezado': 'Crear Contacto',
            'titulo': 'Crear Contacto'
        }
        if request.method == 'GET':
            return render(request, 'contacto.html', render_dict)
        elif request.method == 'POST':
            contactoForm = ContactoForm(request.POST, request.FILES)
            if contactoForm.is_valid():
                contactoForm.save()
                return redirect('editar_contacto', id=contactoForm.instance.id)
            else:
                render_dict['form'] = contactoForm
                return render(request, 'contacto.html', render_dict)
    
    def editar(request, id, tab=None):
        contacto = get_object_or_404(Contacto, id=id)
        if request.method == 'POST':
            contactoForm = ContactoForm(request.POST, request.FILES, instance=contacto)  
            if contactoForm.is_valid():
                contactoForm.save()
                return redirect('editar_contacto', id=contacto.id, tab='contacto')
        
        context = {
            "titulo": "Editar Contacto",
            "encabezado": f"Editar Contacto: {contacto.nombre}",
            "contacto": contacto,
            'form': ContactoForm(instance=contacto),
            'tab': tab
        }
        
        return render(request, 'editar.html', context)
            
    def eliminar(request, id):
        contacto = get_object_or_404(Contacto, id=id)
        if request.method == 'DELETE':
            contacto.delete()
            return JsonResponse({'success': True})

    

    