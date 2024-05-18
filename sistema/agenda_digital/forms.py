from django import forms
from .models import usuario

class usuarioForm(forms.ModelForm):
   class Meta:
      model = usuario
      fields = ['nombre', 'email', 'telefono', 'password']

from .models import *


#crea un formulario con los campos de contacto
class ContactoForm(forms.ModelForm):
    class Meta:
        model = contacto
        
        
        fields = '__all__'
        
       
class BusquedaCategoriaForm(forms.Form):
    nombre = forms.CharField(label='Buscar Categoría', max_length=100, required=False)