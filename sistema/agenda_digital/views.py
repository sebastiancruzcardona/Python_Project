from django.shortcuts import render

# Create your views here.

def index(request):
   #Index view
   return render(request, 'paginas/index.html')

def registro(request):
   #Registro view
   return render(request, 'paginas/registro.html')


