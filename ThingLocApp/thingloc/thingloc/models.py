from django.contrib.auth.models import User
from django.db import models



class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Objeto(models.Model):
    categoria = models.ForeignKey(Categoria)
    nombre = models.CharField(max_length=100)
    recompensa = models.CharField(max_length=100)
    perdido = models.BooleanField(default=True)
    imagen = models.ImageField(max_length=255,upload_to='images') # Este directorio debe residir dentro de MEDIA_URL
    coordenadas = models.CharField(max_length=100)
    usuario = models.ForeignKey(User)




