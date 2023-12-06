"""cree un programa que lea dos numeros
y muestre su producto, su cociente,
su modulo, su suma y su resta."""

n1 = float(input ("Digite un numero: "))
n2 = float(input ("Digite un numero: "))
producto= n1 * n2
cociente = n1 / n2
modulo = abs (n1 - n2) 
"""abs es igual al valor absoluto que es el resultado de la 
operacion tambien se puede sacar con el signo % ejemplo n1 % n2"""
suma = n1 + n2
resta = n1 - n2
print("El producto de los numeros es: ", producto)
print("El cociente de los numeros es: ", cociente)
print("El modulo de la diferencia entre los numeros es: ", modulo)
print("La suma de los numeros es: ", suma)
print("La resta de los numeros es: ", resta)
