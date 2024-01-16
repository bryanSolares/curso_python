from django.db import models


# Create your models here.

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, verbose_name='Nombre')
    apellido_paterno = models.CharField(max_length=40, verbose_name='Apellido Paterno')
    apellido_materno = models.CharField(max_length=40, verbose_name='Apellido Materno')
    direccion = models.TextField(null=True, verbose_name="Dirección")
    creditos = models.CharField(max_length=40, verbose_name='Créditos')
    foto = models.ImageField(upload_to='imagenes/', verbose_name="Foto", null=True)

    def __str__(self):
        fila = "id:" + str(self.id) + ", nombre:" + str(self.nombre) + ", apellido_paterno:" + str(
            self.apellido_paterno) + ", apellido_materno:" + str(self.apellido_materno) + ", direccion:" + str(
            self.direccion) + ", creditos:" + str(self.creditos) + ", foto:" + str(self.foto)
        return fila

    def delete(self, using=None, keep_parents=False):
        self.foto.storage.delete(self.foto.name)
        super().delete()
