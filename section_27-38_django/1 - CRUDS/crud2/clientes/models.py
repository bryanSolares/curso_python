from django.db import models

# Create your models here.
class Lenguaje(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre Lenguaje")


    def __str__(self):
        return self.nombre

class SistemaOperativo(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre SO")

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido_paterno = models.CharField(max_length=100, verbose_name="Apellido Paterno")
    apellido_materno = models.CharField(max_length=100, verbose_name="Apellido Materno")
    foto = models.ImageField(upload_to="imagenes/", verbose_name="Foto", null=False)
    lenguaje = models.ForeignKey(Lenguaje, verbose_name="Lenguaje", on_delete=models.CASCADE)
    sistema_operativo = models.ForeignKey(SistemaOperativo, verbose_name="Sistema Operativo", on_delete=models.CASCADE)

    def __str__(self):
        return "Id" + str(self.id) + "-" + "Nombre" + str(self.nombre)

    def delete(self, using=None, keep_parents=False):
        self.foto.storage.delete(self.foto.name)
        super().delete()