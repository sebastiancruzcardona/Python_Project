from typing import Any
from django.db import models


# Create your models here.
class usuario(models.Model):
   id = models.AutoField(primary_key=True)
   nombre = models.CharField(max_length=60, verbose_name="Nombre")
   email = models.CharField(max_length=60, unique=True, verbose_name="Email")
   telefono = models.CharField(max_length=10, verbose_name="Teléfono")
   password = models.CharField(max_length=50, verbose_name="Contraseña")
   
   #Visualización de datos para el administrador
   def __str__(self):
      fila = f"id: {self.id} | nombre: {self.nombre} | email: {self.email} | telefono: {self.telefono} | password: {self.password}"
      return fila
   
   #Borrado del registro
   def delete(self, using=None, keep_parents=False):
      super().delete()


class contacto(models.Model):
   id = models.AutoField(primary_key=True)
   id_usuario = models.ForeignKey('usuario', on_delete=models.CASCADE)
   nombre = models.CharField(max_length=60, verbose_name="Nombre")
   apellido = models.CharField(max_length=60, verbose_name="Apellido")
   telefono = models.CharField(max_length=10, verbose_name="Teléfono")   
   categoria = models.CharField(max_length=60,null=True, verbose_name="Categoría")
   email = models.CharField(max_length=60, verbose_name="Email")
   favorito = models.BooleanField(default=False, verbose_name="Favorito")   