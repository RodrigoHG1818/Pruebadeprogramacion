import os

metros = float (input ( 'Ingresa el valor de metros: '))
centimetros=metros*100
pulgadas=centimetros/2.54
pies=pulgadas/12
yarda=pies/3
print ('Valor de centimetros: ' + repr (centimetros))
print ('Valor de pies: ' + repr (pies))
print ('Valor de pulgadas: ' + repr (pulgadas))
print ('Valor de yarda: ' + repr (yarda))
print ()
os.system ('pause')