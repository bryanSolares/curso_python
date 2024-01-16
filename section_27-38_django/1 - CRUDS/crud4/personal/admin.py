from django.contrib import admin
from .models import *

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido_paterno', 'apellido_materno', 'area', 'estado')
    search_fields = ["nombre", "apellido_paterno", "apellido_materno"]
    list_filter = ['area', 'estudios']
    list_per_page = 5


admin.site.register(Persona, PersonAdmin)
admin.site.register(Area)
admin.site.register(Estudio)