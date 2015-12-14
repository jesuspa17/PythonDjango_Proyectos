# -*- coding: utf-8 -*-
__author__ = 'Jesus'

from hdad.models import *

#Imprimie los capataces
lista_capataces = Capataz.objects.all()
for capataz in lista_capataces:
    print(capataz)
    print("")

#Imprime las hermandades
lista_hermandades = Hermandad.objects.all()
for hermandad in lista_hermandades:
    print(hermandad)
    print("")

#Imprime la lista de costaleros.
lista_costaleros = Costalero.objects.all()
for costalero in lista_costaleros:
    print(costalero)
    print("")
