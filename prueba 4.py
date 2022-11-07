import os 

centimetros = float (input ('Ingresa el valor de centimetros: '))
pies=centimetros/2.54/12
yardas=pies/3
print ('Valor de pies: ' + repr (pies))
print ('Valor de yardas: ' + repr (yardas))
print ()
os.system ('pause')