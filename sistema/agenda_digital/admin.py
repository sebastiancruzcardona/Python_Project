from django.contrib import admin
from .models import usuario
from .models import contacto

# Register your models here.

admin.site.register(usuario)
admin.site.register(contacto)