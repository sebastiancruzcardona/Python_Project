from django.shortcuts import render

# Create your views here.

def index(request):
   #Index view
   return render(request, 'paginas/index.html')

def registro(request):
   #Registro view
   return render(request, 'paginas/registro.html')


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