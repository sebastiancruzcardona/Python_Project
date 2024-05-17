from django.shortcuts import render, redirect
from .models import contacto, usuario
from .forms import usuarioForm
# Create your views here.

def index(request):
   #Index view
   return render(request, 'paginas/index.html')

def registro(request):
   #Registro view
   formulario = usuarioForm(request.POST or None)
   if formulario.is_valid() and request.POST:
      formulario.save()
      return redirect('index') 
   return render(request, 'paginas/registro.html', {'formulario': formulario})

def editar_usuario(request, id):
   #editar_usurio view
   usuario_editar = usuario.objects.get(id=id)
   formulario = usuarioForm(request.POST or None, instance=usuario_editar) 
   if formulario.is_valid() and request.POST:
      formulario.save()
      return redirect('index')   
   return render(request, 'paginas/editar_usuario.html', {'formulario': formulario})

def agenda(request):
   #Agenda view
   return render(request, 'paginas/agenda.html')

def contactos(request):
   #Contacto view
   return render(request, 'paginas/contactos/index.html')

def crear_contacto(request):
    return render(request, 'paginas/contactos/crear.html')

def editar_contacto(request):
    return render(request, 'paginas/contactos/editar.html')