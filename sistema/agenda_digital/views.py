from django.shortcuts import render, redirect
from .models import contacto, usuario
from .forms import usuarioForm, usuarioLoginForm
from django.http import HttpResponse
from .forms import ContactoForm
from .forms import *
# Create your views here.

def index(request):
   #Index view
   formulario = usuarioLoginForm(request.POST or None)
   if formulario.is_valid() and request.POST:
       email = formulario.cleaned_data.get('email')
       password = formulario.cleaned_data.get('password')
       usuarios = usuario.objects.all()
       id = 0
       for usuario_recorrer in usuarios:
           if email == usuario_recorrer.email and password == usuario_recorrer.password:
               id = usuario_recorrer.id
               
       if id == 0:
           return HttpResponse('Usuario o contraseña no válidos.')
       return redirect('contactos', id) 
         
   return render(request, 'paginas/index.html', {'formulario': formulario})

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
   return render(request, 'paginas/editar_usuario.html', {'formulario': formulario, 'id': id})

def eliminar_usuario(request, email):
   usuario_delete = usuario.objects.get(email=email)
   usuario_delete.delete()
   return redirect('index')

def agenda(request, id):
   #Agenda view
   return render(request, 'paginas/agenda.html')

def contactos(request, id):
   #Contacto view
   #busca todos los contactos creados que tienen el id y retorna un arraylist
   contactos = contacto.objects.filter(id_usuario = id)  
   #retorna la vista contactoss index y el arryalist de contactos
   return render(request, 'paginas/contactos/index.html', {'contactos': contactos, 'id': id})

def crear_contacto(request, id):
    
    formulario = ContactoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid() and request.POST:
        #guarda el formulario en la base de datos
        formulario.save()
        return redirect('contactos', id)
   
   
    return render(request, 'paginas/contactos/crear.html', {'formulario': formulario, 'id': id})

def editar_contacto(request, id):
    #busca el contacto por id y retorna el formulario
    contacto_editar = contacto.objects.get(id=id)
    formulario = ContactoForm(request.POST or None, request.FILES or None, instance=contacto_editar)
    
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('contactos')
    return render(request, 'paginas/contactos/editar.html' , {'formulario': formulario})

def eliminar_contacto(request, id):
   #busca el contacto por id
   contacto_delete = contacto.objects.get(id=id)
   contacto_delete.delete()
   return redirect('contactos')

def buscar_categoria(request, id):
    #Recibe la categoría de la url por get del html contacto index
    categoria = request.GET.get('categoria')
    print(f'La categoría es: {categoria}')  # Imprime el valor de la categoría (categoria)
    # Ahora puedes hacer algo con el valor de la categoría, como buscar en la base de datos
    contactos = contacto.objects.filter(id_usuario = id)
    contactos_buscar = []
    if(categoria == 'Todos'):
        return render(request, 'paginas/contactos/index.html',  {'contactos': contactos, 'id': id})
    else:
      for contacto1 in contactos:
        if contacto1.categoria == categoria:
            contactos_buscar.append(contacto1)
    contactos = contactos_buscar
    
    return render(request, 'paginas/contactos/index.html',  {'contactos': contactos, 'id': id})


def buscar_favoritos(request, id):
    #busca los contactos favoritos
    contactos = contacto.objects.filter(id_usuario = id) 
    contactos_favorites = []
    for contacto1 in contactos:
        if contacto1.favorito == True:
            contactos_favorites.append(contacto1)

    contactos = contactos_favorites          
    return render(request, 'paginas/contactos/index.html',  {'contactos': contactos, 'id': id})
