"""Cree un programa que reciba tres números y muestre el mayor. En caso de que los números sean iguales también se debe mostrar al usuario."""

n1=float(input("Ingrese el primer numero: "))
n2=float(input("Ingrese el segundo numero: "))
n3=float(input("Ingrese el tecer numero: "))

if n1>n2 and n1>n3:
    print(str(n1) + " Es mayor a " + str(n2) + " y " + str(n3))

elif n2>n1 and n2>n3:
    print(str(n2) + " Es mayor a " + str(n1) + " y " + str(n3))
    
elif n3>n1 and n3>n2:
    print(str(n3) + " Es mayor a " + str(n1) + " y " + str(n2))

else:
    print("Los numero son iguales")