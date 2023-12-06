"""Cree un programa que tome el radio de un círculo e imprima su área y perímetro"""

pi=3.1416
radio=float(input("Ingrese el radio del circulo: "))
perimetro= 2 * pi * radio
area = pi * radio ** 2

print("El area del circulo es: " + str(area))
print("El perimetro del circulo es: " + str(perimetro))