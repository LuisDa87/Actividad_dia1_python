"""7. Mayor de Dos Números
Pide dos números al usuario. Imprime cuál es el mayor. Si son iguales, indícalo."""

numero1=int(input("ingrese un numero: "))
numero2=int(input("ingrese un segundo numero: "))

if numero1>numero2:
    print("el numero mayor es ", numero1)

elif numero1==numero2:   
    print("los numeros son iguales")
else: 
    print("el numero mayor es", numero2)