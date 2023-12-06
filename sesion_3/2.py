"""En un supermercado se tiene los siguientes productos: lentejas, crema, arroz y vino. Las lentejas y el arroz no pagan IVA, el vino y la crema si. Cree un programa que reciba el nombre de alguno de los productos mencionados y muestre si el producto paga IVA o no"""

print("LOS PRODUCTOS SON: lentejas - crema - arroz - vino. ")
producto = input("ingrese producto: ")
if producto == "lentejas" or producto == "arroz" or producto == "crema" or producto == "vino":
    if producto == "lentejas" or producto == "arroz":
        print("No paga iva")
    else:
        print("Paga iva ")
else:
    print("Ingrese un producto valido")