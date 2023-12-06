#Cree un programa que dado un número entero n, calcule su factorial(n!).

def factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

num = int(input("Introduzca un número entero: "))

resultado = factorial(num)
print("El factorial de", num, "es", resultado)