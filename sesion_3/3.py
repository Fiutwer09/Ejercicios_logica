"""Cree un programa que reciba dos números y muestre el mayor. En caso de que los números sean iguales también se debe mostrar al usuario."""

n1=float(input("Ingrese el primer numero: "))
n2=float(input("Ingrese el segundo numero: "))

if n1>n2:
    print(str(n1) + " Es mayor a " + str(n2))

elif n2>n1:
    print(str(n2) + " Es mayor a " + str(n1))

else:
    print("Los numero son iguales")