from django.shortcuts import render, redirect
from .models import contacto, usuario
from .forms import usuarioForm
from django.http import HttpResponse
from .forms import ContactoForm
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
   #busca todos los contactos creados y retorna un arraylist
   contactos = contacto.objects.all()
   
   #retorna la vista contactoss index y el arryalist de contactos
   return render(request, 'paginas/contactos/index.html', {'contactos': contactos})

def crear_contacto(request):
    
    formulario = ContactoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        #guarda el formulario en la base de datos
        formulario.save()
        return redirect('contactos/index.html')
   
   
    return render(request, 'paginas/contactos/crear.html', {'formulario': formulario})

def editar_contacto(request, id):
    #busca el contacto por id y retorna el formulario
    contacto = contacto.objects.get(id=id)
    formulario = ContactoForm(request.POST or None, request.FILES or None, instance=contacto)
    
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('contactos/index.html')
    return render(request, 'paginas/contactos/editar.html' , {'formulario': formulario})

def eliminar_contacto(request, id):
   #busca el contacto por id
   contacto = contacto.objects.get(id=id)
   contacto.delete()
   return redirect('contactos/index.html')