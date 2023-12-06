"""Cree un programa que lea los tres ángulos internos de un triángulo y muestre si los ángulos corresponden a un triángulo o no"""

ang1=int(input("Ingrese el primer angulo: "))
ang2=int(input("Ingrese el segundo angulo: "))
ang3=int(input("Ingrese el tercer angulo: "))

triangulo= ang1 + ang2 + ang3
if triangulo==180:
    print ("Los angulos forman un triangulo")
else:
    print ("No son los angulos de un triangulo")