"""Cree un programa que lea un número entre 1 y 15 y muestre si éste es primo o no"""

p2=2
p3=3
p5=5
p7=7
p11=11
p13=13
print("Ingrese un numero del 1 al 15: ")
n = int(input("Ingrese el numero: "))
if n>15 or n<1:
    print("¡ERROR! - Numero incorrecto")
elif n==p2 or n==p3 or n==p5 or n==p7 or n==p11 or n==p13:
    print(str(n)+" Es Primo")
else:
    print(str(n)+" No es primo")