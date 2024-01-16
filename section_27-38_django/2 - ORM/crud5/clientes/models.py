from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Base(models.Model):
    status = models.BooleanField(default=True, verbose_name="Status")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Date Created")
    updated_date = models.DateTimeField(default=timezone.now, verbose_name="Date Updated")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")

    class Meta:
        abstract = True


class Author(Base):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Area(Base):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Area")

    def __str__(self):
        return self.name


class EducationLevel(Base):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Level Education")

    def __str__(self):
        return self.name


degree = (
    ("Sistemas", "Sistemas"),
    ("Derecho", "Derecho"),
    ("Contabilidad", "Contabilidad"),
    ("Administración", "Administración")
)


class Customer(Base):
    name = models.CharField(max_length=50, blank=False, null=False, verbose_name="Name")
    last_name_1 = models.CharField(max_length=50, blank=False, null=False, verbose_name="Last name 1")
    last_name_2 = models.CharField(max_length=50, blank=False, null=False, verbose_name="Last name 2")
    img = models.ImageField(upload_to="imagenes/", blank=True, null=True, verbose_name="Image")
    area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name="Area")
    education = models.CharField(max_length=50, choices=degree, verbose_name="Education")
    degree = models.CharField(max_length=50, choices=degree, verbose_name="Degree")

    def __str__(self):
        return self.name + " " + self.last_name_1 + " " + self.last_name_2

    def delete(self, using=None, keep_parents=False):
        if self.foto:
            self.foto.storage.delete(self.foto.name)

        super().delete(using=using, keep_parents=keep_parents)
