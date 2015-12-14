from django.db import models

class Capataz(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    poblacion = models.CharField(max_length=100)
    calle = models.CharField(max_length=100)

    def __str__(self):
        return "Nombre: " +self.nombre+\
               "\nApellidos: " +self.apellidos+\
               "\nPronvincia: "+self.provincia+ \
               "\nPoblacion: " +self.poblacion+\
               "\nCalle: "+self.calle

    class Admin():
        pass

class Hermandad(models.Model):
    nombre = models.CharField(max_length=100)
    num_hermanos = models.CharField(max_length=100000)
    hermano_mayor = models.CharField(max_length=50)
    dia_salida = models.CharField(max_length=50)
    capataz = models.ForeignKey(Capataz)

    def __str__(self):
        return "Nombre: " +self.nombre+\
               "\nNum Hermanos: " +self.num_hermanos+\
               "\nHermano mayor: "+self.hermano_mayor+ \
               "\nDia de salida: " +self.dia_salida+\
               "\nCapataz[ "+self.capataz.__str__() +"]"

    class Admin():
        pass

class Costalero(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    poblacion = models.CharField(max_length=100)
    calle = models.CharField(max_length=100)
    hermandad = models.ForeignKey(Hermandad)

    def __str__(self):
        return "Nombre: " +self.nombre+\
               "\nApellidos: " +self.apellidos+\
               "\nProvincia: "+self.provincia+ \
               "\nPoblacion: " +self.poblacion+\
               "\nHermandad[ "+self.hermandad.__str__() +"]"

    class Admin():
        pass
