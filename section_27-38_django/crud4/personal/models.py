from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from clientes.models import DatosBase


# Create your models here.
class Area(DatosBase):
    nombre_area = models.CharField(max_length=100, verbose_name="Nombre de Area", null=False, blank=False)

    def __str__(self):
        return self.nombre_area


class Estudio(DatosBase):
    nombre_estudio = models.CharField(max_length=100, verbose_name="Nombre Estudio", null=False, blank=False)

    def __str__(self):
        return self.nombre_estudio


carrera = (('Sistemas', 'Sistemas'),
           ('Derecho', 'Derecho'),
           ('Contabilidad', 'Contabilidad'),
           ('Administración', 'Administración'))


class Persona(DatosBase):
    nombre = models.CharField(max_length=100, verbose_name="Nombre", null=False, blank=False)
    apellido_paterno = models.CharField(max_length=100, verbose_name="Apellido Paterno", null=False, blank=False)
    apellido_materno = models.CharField(max_length=100, verbose_name="Apellido Materno", null=False, blank=False)
    foto = models.FileField(upload_to='imagenes/', verbose_name="Fotografía", null=True, blank=True)
    area = models.ForeignKey(Area, verbose_name="Area", on_delete=models.CASCADE)
    estudios = models.ForeignKey(Estudio, verbose_name="Estudios", on_delete=models.CASCADE)
    carrera = models.CharField(max_length=100, choices=carrera, verbose_name="Carrera", null=False, blank=False)

    def __str__(self):
        return str(self.id) + " - " + self.nombre + " - " + self.apellido_paterno + " - " + self.apellido_materno

    def delete(self, using=None, keep_parents=False):
        if self.foto:
            self.foto.storage.delete(self.foto.name)

        super().delete(using=using, keep_parents=keep_parents)
