from django import forms
from ..models import Telefono

class TelefonoForm(forms.ModelForm):
    class Meta:
        model = Telefono
        fields = ['contacto', 'tipo', 'alias', 'numero']
        
        widgets = {
            'contacto': forms.Select(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'alias': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Teléfono personal'}),
            'numero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 55-1234-5678'}),
        }
        
        labels = {
            'contacto': 'Contacto',
            'tipo': 'Tipo de Teléfono',
            'alias': 'Alias',
            'numero': 'Número de Teléfono',
        }