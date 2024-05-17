from django.urls import path
from . import views

urlpatterns = [
   #Path for index view
   path('', views.index, name='index'),
   
   #Path for registro view
   path('registro', views.registro, name='registro'),
   
   #Path for editar_usuario view
   path('editar_usuario', views.editar_usuario, name='editar_usuario'),

   path('agenda', views.agenda, name='agenda'),

   path('contactos', views.contactos, name='contactos'),

   path('contactos/crear', views.crear_contacto, name='crear'),

   

   path('contactos/editar/<int:id>', views.editar_contacto, name='editar'),
   
   path('contactos/eliminar/<int:id>', views.eliminar_contacto, name='eliminar'),
]
