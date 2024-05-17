from django import forms

from .models import *

class ContactoForm(forms.ModelForm):
    class Meta:
        model = contacto
        fields = '__all__'
        widget = {
            'favorito': forms.CheckboxInput()
        }
