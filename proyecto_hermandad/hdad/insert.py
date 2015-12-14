# -*- coding: utf-8 -*-
__author__ = 'Jesus'

from hdad.models import *

#Creación de capataces.
c1 = Capataz(nombre = 'Antonio', apellidos ='Santiago Muñoz', provincia = 'Sevilla', poblacion = 'Umbrete', calle = 'C/Los Desamparados 15')
c2 = Capataz(nombre = 'Antonio', apellidos ='Villanueva', provincia = 'Sevilla', poblacion = 'Sevilla', calle = 'C/Feria 15')
c3 = Capataz(nombre = 'Juan Jesús', apellidos ='Vázquez Rodríguez', provincia = 'Sevilla', poblacion = 'Olivares', calle = 'C/Conde Duque 5')

c1.save()
c2.save()
c3.save()

#Creacion de hermandades asociandole algunos de los capataces creados anteriormente.
h1 = Hermandad(nombre = "La Paz", num_hermanos='800', hermano_mayor = 'Juan Perera', dia_salida = 'Domingo de Ramos', capataz = c1)
h2 = Hermandad(nombre = "Cristo de Burgos", num_hermanos='500', hermano_mayor = 'Ernesto Sanguino', dia_salida = 'Miércoles Santo', capataz = c1)
h3 = Hermandad(nombre = "Las Penas de San Vicente", num_hermanos='800', hermano_mayor = 'Benito Quintero', dia_salida = 'Lunes Santo', capataz = c1)
h4 = Hermandad(nombre = "La Amargura", num_hermanos='1500', hermano_mayor = 'Pepe Talega', dia_salida = 'Domingo de Ramos', capataz = c2)
h5 = Hermandad(nombre = "San Bernardo", num_hermanos='1600', hermano_mayor = 'Morante de la Puebla', dia_salida = 'Miércoles Santo', capataz = c2)

h1.save()
h2.save()
h3.save()
h4.save()
h5.save()

#Creación de costaleros asociandole su hermandad
c1 = Costalero(nombre = 'Jesús', apellidos ='Pallares Suárez', provincia = 'Sevilla', poblacion = 'Olivares', calle = 'C/Cristobal Colón 14', hermandad = h3)
c2 = Costalero(nombre = 'Jordi', apellidos ='Vázquez Ciero', provincia = 'Sevilla', poblacion = 'Olivares', calle = 'C/PioX 10', hermandad = h3)
c3 = Costalero(nombre = 'Pablo', apellidos ='Moguer', provincia = 'Sevilla', poblacion = 'Olivares', calle = 'Plaza Jesús Nazareno 1', hermandad = h5)
c4 = Costalero(nombre = 'Francisco', apellidos ='Lindes', provincia = 'Sevilla', poblacion = 'Olivares', calle = 'C/ Perpetuo Socorro', hermandad = h4)

c1.save()
c2.save()
c3.save()
c4.save()


