from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import contacto
from .forms import ContactoForm
# Create your views here.

def index(request):
   #Index view
   return render(request, 'paginas/index.html')

def registro(request):
   #Registro view
   return render(request, 'paginas/registro.html')

def editar_usuario(request):
   #editar_usurio view
   return render(request, 'paginas/editar_usuario.html')


def agenda(request):
   #Agenda view
   return render(request, 'paginas/agenda.html')

def contactos(request):
   #Contacto view
   contactos = contacto.objects.all()
   return render(request, 'paginas/contactos/index.html', {'contactos': contactos})

def crear_contacto(request):
    
    formulario = ContactoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        
        formulario.save()
        return redirect('contactos/index.html')
   
   
    return render(request, 'paginas/contactos/crear.html', {'formulario': formulario})

def editar_contacto(request):
    return render(request, 'paginas/contactos/editar.html')

def eliminar_contacto(request, id):
   contacto = contacto.objects.get(id=id)
   contacto.delete()
   return redirect('contactos/index.html')