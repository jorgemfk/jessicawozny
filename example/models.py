from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)

class Exposicion(models.Model):
    TIPO_CHOICES = [
        ('Colectiva', 'Colectiva'),
        ('Individual', 'Individual'),
    ]

    año = models.IntegerField()
    nombre_exposicion = models.CharField(max_length=255)
    lugar = models.CharField(max_length=255)
    estado = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    curaduria = models.CharField(max_length=150, blank=True, null=True)
    def __str__(self):
        return f"{self.nombre_exposicion} ({self.año})"

class PremioDistincion(models.Model):
    año = models.CharField(max_length=9)  # Ejemplo: "2021/2024"
    distincion = models.CharField(max_length=255)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.año} - {self.distincion} ({self.pais})"

class GifAnimacion(models.Model):
    imagen = models.ImageField(upload_to='gifs/')
    creado = models.DateTimeField(auto_now_add=True)

class Gif(models.Model):
    archivo = models.ImageField(upload_to='gifs/')
    creado = models.DateTimeField(auto_now_add=True)
