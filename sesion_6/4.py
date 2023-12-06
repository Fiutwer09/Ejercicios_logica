#Cree un programa que muestre los números impares entre 1 y n.

def mostrar_numeros_impares(n):
  for i in range(1, n + 1):
    if i % 2 == 1:
      print(i)
n = int(input("Ingrese un número: "))

mostrar_numeros_impares(n)