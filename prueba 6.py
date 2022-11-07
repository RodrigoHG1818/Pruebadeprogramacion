import os

precio_del_producto = float (input ('Ingresa el valor de precio del producto: '))
IGV=precio_del_producto*0.18
print ('Valor de IGV: ' + repr (IGV))
print ()
os.system ('pause')