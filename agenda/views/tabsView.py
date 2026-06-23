from django.shortcuts import get_object_or_404, render
from django.views.generic import View
from agenda.forms.contactoForms import ContactoForm
from agenda.forms.direccionForm import DireccionForm
from agenda.forms.telefonoForm import TelefonoForm
from agenda.forms.telefonoFormSet import TelefonoFormSet
from agenda.models import Contacto

class TabsView(View):
    def get(self, request, id, tab):
        contacto = get_object_or_404(Contacto, id=id)
    
        if tab == 'contacto':
            contactoForm = ContactoForm(instance=contacto)
            return render(request, 'tabs/contacto_tab.html', {
                'contacto': contacto,
                'form': contactoForm
            })
        
        elif tab == 'direccion':
            direccion = contacto.direccion_set.first()
            direccionForm = DireccionForm(instance=direccion) if direccion else DireccionForm(initial={'contacto': contacto})
            return render(request, 'tabs/direccion_tab.html', {
                'contacto': contacto,
                'form': direccionForm,
                'direccion': direccion
            })
        
        elif tab == 'telefono':
            formset = TelefonoFormSet(instance=contacto)
            return render(request, 'tabs/telefono_tab.html', {
                'contacto': contacto,
                'formset': formset,
                'tab': tab
            })
