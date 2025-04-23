"""
6. Adivina el Número
Fija un número secreto (por ejemplo, 7). Pide al usuario que lo adivine.
Di si su número es mayor, menor o igual al número secreto.

"""
num_secret=8

num=int(input("Ingrese un numero: "))

if num<num_secret:
    print("su numero es menor < ")
elif num>num_secret:
    print("su numero es mayor >")
else:
    print("el numero es igual = ")