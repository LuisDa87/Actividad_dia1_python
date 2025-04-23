"""10. Número Dentro de Rango
Pide un número al usuario. Di si está dentro del rango de 1 a 10 (inclusive).
"""

num=int(input("INgrese un numero: "))

if num >= 1 and num>=10:
    print("El numero esta en el rango: ", num )
else:
    print("Numero fuera del rango: ", num )