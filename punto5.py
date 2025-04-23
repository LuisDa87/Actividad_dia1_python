"""
5. Calculadora de Propinas
Pide al usuario el total de una cuenta. Luego pregunta qué porcentaje de propina quiere dejar 
(10, 15 o 20). Calcula y muestra el valor de la propina.
""" 

cuenta=int(input("Ingrese el total de la cuenta $: "))

propina=int(input("Ingrese el porcentaje de propina elije entre 10% o 15% o 20%: "))

total=cuenta*(propina/100)

print("El valor de la propina es $: ", total)
