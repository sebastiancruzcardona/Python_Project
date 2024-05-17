from django import forms

from .models import *


#crea un formulario con los campos de contacto
class ContactoForm(forms.ModelForm):
    class Meta:
        model = contacto
        
        
        fields = 'id_usuario', 'nombre', 'apellido', 'telefono', 'email', 'favorito'
        
        witghts = {
            'id_usuario': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'favorito': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
