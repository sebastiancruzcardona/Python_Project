from django.db import models

# Create your models here.
class usuario(models.Model):
   id = models.AutoField(primary_key=True)
   nombre = models.CharField(max_length=60)
   email = models.CharField(max_length=60)
   telefono = models.CharField(max_length=10)
   password = models.CharField(max_length=50)