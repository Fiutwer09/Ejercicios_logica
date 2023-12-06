#Cree un programa que calcule la suma de los cuadrados de los números entre 1 y n

def suma_cuadrados(n):
    suma = 0

    for i in range(1, n + 1):
        suma += i**2

    return suma

if __name__ == "__main__":
    try:
        n = int(input("Ingresa un número: "))
    except ValueError:
        print("Por favor, ingresa un número entero válido.")
    else:
        resultado = suma_cuadrados(n)
        print(f"La suma de los cuadrados de los números entre 1 y {n} es: {resultado}")
