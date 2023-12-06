"""cree un programa que lea la edad de un usuario y 
muestre cuantos años tendra el usuario dentro de tantos 
como el usuario indique """

edad = int(input("Ingrese su edad: "))
años = int(input("Ingrese dentro de cuantos años desea saber su edad: "))

total = edad + años

print ("Su edad dentro de " + str(años) + " años, sera de: " + str(total) + " años")