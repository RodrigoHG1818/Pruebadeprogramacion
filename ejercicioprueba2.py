#Ejercicioprueba2

import os

matricula = input ('Ingresa el matricula: ')
nombre = input ('Ingresa el nombre: ')
calificacion_1 = float (input ('Ingresa el valor de calificacion 1: '))
calificacion_2 = float (input ('Ingresa el valor de calificacion 2: '))
calificacion_3 = float (input ('Ingresa el valor de calificacion 3: '))
promedio=(calificacion_1+calificacion_2+calificacion_3)/3
print ('Matricula: ' + matricula)
print ('Nombre: ' + nombre)
print ('Valor de promedio: ' + repr (promedio))
print ()
os.system ('pause')