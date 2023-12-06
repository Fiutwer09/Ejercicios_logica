""""
Crea un programa que tome el precio de un producto e imprima su precio final al consumidor con un IVA de 19%
"""
iva = 0.19 
nombre_producto = input("ingrese nombre de producto: ")
valor_producto = float(input("ingrese valor producto: " ))

ipc= valor_producto * iva
valor_total = valor_producto + ipc

print("El valor total a pagar sin IVA es: " + str(valor_producto))
print("El IVA es: " + str(ipc))
print("El valor total a pagar con IVA es: " + str(valor_total))
