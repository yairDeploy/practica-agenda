

from django.views import View
from agenda.forms.direccionForm import DireccionForm
from agenda.models import Direccion
from django.shortcuts import redirect


class DireccionView(View):
    
    def post(self,request):
        id = request.POST.get('contacto')[0]
        direccion = Direccion.objects.filter(contacto_id=id).first() 
        if direccion:
            direccionForm = DireccionForm(request.POST, instance=direccion)
        else:
            direccionForm = DireccionForm(request.POST) 
        if direccionForm.is_valid():
            direccionForm.save()
            return redirect('editar_contacto', id=id, tab='direccion')
        else:
            print("Error al guardar la dirección:", direccionForm.errors)
            return redirect('editar_contacto', id=id, tab='direccion')