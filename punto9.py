"""9. Año Bisiesto
Pide un año al usuario. Determina si es bisiesto 
(es divisible entre 4 y no entre 100, excepto si también es divisible entre 400)."""


year=int(input("ingrese el año: "))

op=year%4 
op2=year%100
op3=year%400

if op==0 and op2!=0:
    print("es un año bisiesto")
elif op3%400==0: 
    print("No es biciesto")
else:
    print("No es biciesto")

