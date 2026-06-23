from django import forms
from ..models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'
        
        widgets = {
            'fecha_nacio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese los apellidos'}),
            'fotografia': forms.FileInput(attrs={'class': 'form-control-file'}),
        }
        
        labels = {
            'nombre': 'Nombre*',
            'apellidos': 'Apellidos*',
            'fotografia': 'Fotografía*',
            'fecha_nacio': 'Fecha de Nacimiento',
        }