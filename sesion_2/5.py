"""
Cree un programa que tome el valor de un producto e imprima su precio final si este tiene siempre un descuento del 10%
"""
descuento = 0.10
producto = input("ingrese nombre del producto: ")
valor_producto = float(input("ingrese precio del producto: "))

valor_descuento = valor_producto * descuento
valor_total = valor_producto - valor_descuento

print ("El total a pagar sin descuento es: " + str(valor_producto))
print ("El valor del descuento es: " + str(valor_descuento))
print ("El total a pagar con descuento es:" + str(valor_total))


