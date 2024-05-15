from django.db import models

# Create your models here.
class usuario(models.Model):
   id = models.AutoField(primary_key=True)
   nombre = models.CharField(max_length=60, verbose_name="Nombre")
   email = models.CharField(max_length=60, verbose_name="Email")
   telefono = models.CharField(max_length=10, verbose_name="Teléfono")
   password = models.CharField(max_length=50, verbose_name="Contraseña")