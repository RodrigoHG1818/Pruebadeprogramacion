import os

altura = float (input ('Ingresa el valor de altura:'))
base = float (input ('Ingresa el valor de base: '))
area=altura*base
perimetro=altura+base
print ('Valor de area: ' + repr (area))
print ('Valor de perimetro: ' + repr (perimetro))
print ()
os.system ('pause')
