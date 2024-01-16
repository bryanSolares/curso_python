from django.contrib import admin
from .models import *
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_per_page = 5

admin.site.register(Author)
admin.site.register(Area)
admin.site.register(EducationLevel)
admin.site.register(Customer, CustomerAdmin)