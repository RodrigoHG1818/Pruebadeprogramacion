numero_ingresado = (input("Ingrese un numero "))
revertir = 0
try:
    valor= int(numero_ingresado)
    while valor > 0:
        residuo = valor % 10
        revertir = (revertir * 10) + residuo
        valor //= 10
    print('El inverso del numero ingresado es: ', revertir)
except ValueError:
    print("Ese numero no es valido. Intentalo de nuevo !")
