from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre}, {self.numero_pasaporte}, {self.fecha_nacimiento}, {self.id}"


class FamiliarHobbie(models.Model):
    nombre = models.CharField(max_length=100)
    hobbie = models.CharField(max_length=500)

class FamiliarProfesion(models.Model):
    nombre = models.CharField(max_length=100)
    profesion = models.CharField(max_length=500)


class Configuracion(models.Model):
    nombre_blog = models.CharField(max_length=14)
    construido_por = models.CharField(max_length=30, default='')
    titulo_principal = models.CharField(max_length=30, default='')
    subtitulo_principal = models.CharField(max_length=60, default='')
