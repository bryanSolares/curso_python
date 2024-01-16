from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class DatosBase(models.Model):
    estado = models.BooleanField(default=False, verbose_name="estado")
    fecha_registro = models.DateTimeField(auto_now_add=timezone.now(), verbose_name="Fecha de Registro")
    fecha_modificacion = models.DateTimeField(auto_now=timezone.now(), verbose_name="Fecha de Modificación")
    usuario = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE)

    class Meta:
        abstract = True