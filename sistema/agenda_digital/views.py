from django.shortcuts import render

# Create your views here.

def index(request):
   #Index view
   return render(request, 'paginas/index.html')

def agenda(request):
   #Agenda view
   return render(request, 'paginas/agenda.html')
