from django import forms
from ..models import Direccion

class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ['contacto', 'calle', 'numero_exterior', 'numero_interior', 
                  'colonia', 'municipio', 'estado', 'referencias']
        
        widgets = {
            'contacto': forms.HiddenInput(),
            'calle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Calle'}),
            'numero_exterior': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número exterior'}),
            'numero_interior': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número interior'}),
            'colonia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Colonia'}),
            'municipio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Municipio'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'referencias': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Referencias'}),
        }
        
        labels = {
            'calle': 'Calle*',
            'numero_exterior': 'Número Exterior*',
            'numero_interior': 'Número Interior*',
            'colonia': 'Colonia*',
            'municipio': 'Municipio*',
            'estado': 'Estado*',
            'referencias': 'Referencias*',
        }
        