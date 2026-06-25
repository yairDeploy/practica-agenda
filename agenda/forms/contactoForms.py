from django import forms
from ..models import Contacto

class ContactoForm(forms.ModelForm):
    fecha_nacio = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control'},
            format='%Y-%m-%d'
        ),
        input_formats=['%Y-%m-%d']
    )
    class Meta:
        model = Contacto
        fields = '__all__'
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese los apellidos'}),
        }
        
        labels = {
            'nombre': 'Nombre*',
            'apellidos': 'Apellidos*',
            'fotografia': 'Fotografía*',
            'fecha_nacio': 'Fecha de Nacimiento',
        }