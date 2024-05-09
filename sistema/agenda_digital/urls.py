from django.urls import path
from . import views

urlpatterns = [
   #Path for index view
   path('', views.index, name='index'), 

   path('agenda', views.agenda, name='agenda'),
]
