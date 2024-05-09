from django.urls import path
from . import views

urlpatterns = [
   #Path for index view
   path('', views.index, name='index'),
   
   #Path for registro view
   path('registro', views.registro, name='registro'), 
]