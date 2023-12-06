#Cree un programa que calcula la suma de los primeros n números naturales.

def suma_primeros_n_naturales(n):
  suma = 0
  for i in range(1, n + 1):
    suma += i

  return suma
n = int(input("Ingrese un número: "))

print(f"La suma de los primeros {n} números naturales es {suma_primeros_n_naturales(n)}")