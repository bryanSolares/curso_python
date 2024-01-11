from django.contrib import admin
from .models import *

#Esto no está bien explicado en el curso
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido_paterno', 'apellido_materno', 'foto', 'lenguaje', 'sistema_operativo', 'area']
    search_fields = ['nombre', 'apellido_paterno', 'apellido_materno']
    list_filter = ['lenguaje', 'area']
    list_per_page = 5


# Register your models here.
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(SistemaOperativo)
admin.site.register(Lenguaje)