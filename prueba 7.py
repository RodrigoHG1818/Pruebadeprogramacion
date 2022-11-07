import os

compra = float (input ('Ingresa el valor de compra: '))
if compra>=100000:
    descuento=compra*0.25
else:
    descuento=0
total=compra-descuento
print ('Valor de descuento: '+ repr (descuento))
print ('Valor de total: ' + repr (total))
print ()
os.system ('pause')