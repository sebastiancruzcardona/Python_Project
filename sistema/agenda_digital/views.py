from django.shortcuts import render, redirect
from .models import contacto, usuario
from .forms import usuarioForm, usuarioLoginForm
from django.http import HttpResponse
from .forms import ContactoForm
from .forms import *
from .exceptions import *
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
       nombre = formulario.cleaned_data.get('nombre')
       correo = formulario.cleaned_data.get('email')
       telefono = formulario.cleaned_data.get('telefono')
       try:
           validar_campos2(nombre = nombre, email = correo, telefono = telefono)       
       except Nombre_No_Debe_Contener_numeros as e:
           return HttpResponse(f'Error en el registro. {e}')
       except Email_No_Valido as e:
           return HttpResponse(f'Error en el registro. {e}')
       except Telefono_No_Valido as e:
           return HttpResponse(f'Error en el registro. {e}')             
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
   all_categorias =[]
   for categoria in contactos:
       all_categorias.append(categoria.categoria)

   categorias = set(all_categorias)
   #retorna la vista contactoss index y el arryalist de contactos
   return render(request, 'paginas/contactos/index.html', {'contactos': contactos, 'id': id, 'all_categorias': categorias})

def crear_contacto(request, id):
    
    formulario = ContactoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid() and request.POST:
       
       nombre = formulario.cleaned_data.get('nombre')
       apellido = formulario.cleaned_data.get('apellido')
       correo = formulario.cleaned_data.get('email')
       telefono = formulario.cleaned_data.get('telefono')
       try:
           validar_campos2(nombre = nombre, email = correo, telefono = telefono, apellido = apellido)       
       except Nombre_No_Debe_Contener_numeros as e:
           return HttpResponse(f'Error en el registro. {e}')
       except Apellido_No_Debe_Contener_numeros as e:
           return HttpResponse(f'Error en el registro. {e}')
       except Email_No_Valido as e:
           return HttpResponse(f'Error en el registro. {e}')
       except Telefono_No_Valido as e:
           return HttpResponse(f'Error en el registro. {e}')      
        
       formulario.save()
       return redirect('contactos', id)   
   
    return render(request, 'paginas/contactos/crear.html', {'formulario': formulario, 'id': id})

def editar_contacto(request, id, id2):
    #busca el contacto por id y retorna el formulario
    contacto_editar = contacto.objects.get(id=id2)
    formulario = ContactoForm(request.POST or None, request.FILES or None, instance=contacto_editar)
    
    if formulario.is_valid() and request.POST:
        nombre = formulario.cleaned_data.get('nombre')
        apellido = formulario.cleaned_data.get('apellido')
        correo = formulario.cleaned_data.get('email')
        telefono = formulario.cleaned_data.get('telefono')
        try:
            validar_campos(nombre = nombre, email = correo, telefono = telefono, apellido = apellido)       
        except Nombre_No_Debe_Contener_numeros as e:
           return HttpResponse(f'Error en el la edición. {e}')
        except Apellido_No_Debe_Contener_numeros as e:
           return HttpResponse(f'Error en el la edición. {e}')
        except Email_No_Valido as e:
           return HttpResponse(f'Error en el la edición. {e}')
        except Telefono_No_Valido as e:
           return HttpResponse(f'Error en el la edición. {e}')
        formulario.save()
        return redirect('contactos', id)
    return render(request, 'paginas/contactos/editar.html' , {'formulario': formulario, 'id': id})

def eliminar_contacto(request, id, id2):
   #busca el contacto por id
   contacto_delete = contacto.objects.get(id=id2)
   contacto_delete.delete()
   return redirect('contactos', id)

def buscar_categoria(request, id):
    #Recibe la categoría de la url por get del html contacto index
    categoria = request.GET.get('categoria')
    print(f'La categoría es: {categoria}')  # Imprime el valor de la categoría (categoria)
    # Ahora puedes hacer algo con el valor de la categoría, como buscar en la base de datos
    contactos = contacto.objects.filter(id_usuario = id)
    contactos_buscar = []

    all_categorias =[]
    for categoria1 in contactos:
        all_categorias.append(categoria1.categoria)

    categorias = set(all_categorias)    
    
    if(categoria == 'Todos'):
        return render(request, 'paginas/contactos/index.html',  {'contactos': contactos, 'id': id, 'all_categorias': categorias} )
    else:
      for contacto1 in contactos:
        if contacto1.categoria == categoria:
            contactos_buscar.append(contacto1)
    contactos = contactos_buscar
    
    return render(request, 'paginas/contactos/index.html',  {'contactos': contactos, 'id': id, 'all_categorias': categorias})


def buscar_favoritos(request, id):
    #busca los contactos favoritos
    contactos = contacto.objects.filter(id_usuario = id) 
    contactos_favorites = []
    all_categorias =contactos
    for contacto1 in contactos:
        if contacto1.favorito == True:
            contactos_favorites.append(contacto1)

    contactos = contactos_favorites          
    return render(request, 'paginas/contactos/index.html',  {'contactos': contactos, 'id': id, 'all_categorias': all_categorias})


def buscar_nombre(request, id):
   nombre_get = request.GET.get('name')
   
   contactos = contacto.objects.filter(id_usuario = id)
   all_categorias = [] 
   for categoria in contactos:
       all_categorias.append(categoria.categoria)

   categorias = set(all_categorias)
   
   contactos_filtrados = []
   
   for contacto1 in contactos:
      if contacto1.nombre.lower().find(nombre_get) != -1:
         contactos_filtrados.append(contacto1)
         
   
   contactos = contactos_filtrados


   
   
   return render(request, 'paginas/contactos/index.html',  {'contactos': contactos, 'id': id, 'all_categorias': categorias})

#Validaciones de campos

#Para poder manejar expresiones regulares
import re

#Validación nombre
def validar_nombre(texto):
    #any evalúa un iterable
    if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]+$', texto):
        raise Nombre_No_Debe_Contener_numeros()

#Validación apellido    
def validar_apellido(texto):
    if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]+$', texto):
        raise Apellido_No_Debe_Contener_numeros()

#Validación email
def validar_email(email: str) -> None:
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        raise Email_No_Valido()

#Validación de telefono    
def validar_telefono(telefono):
    if len(telefono) != 10 or not telefono.isdigit():
        raise Telefono_No_Valido()
    
#Validación general para llamar en las views empleando if y elif
def validar_campos(**campos):
    for campo, valor in campos.items():
        if campo == 'nombre':
            validar_nombre(valor)
        elif campo == 'email':
            validar_email(valor)
        elif campo == 'telefono':
            validar_telefono(valor) 
        elif campo == 'apellido':
            validar_apellido(valor)
            
#Validación general para llamar en las views empleando match case          
def validar_campos2(**campos):
    for campo, valor in campos.items():
        match campo:
            case 'nombre':
                validar_nombre(valor)
            case 'email':
                validar_email(valor)
            case 'telefono':
                validar_telefono(valor) 
            case 'apellido':
                validar_apellido(valor)
            
    
