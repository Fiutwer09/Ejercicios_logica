"""Cree un programa que pregunte al usuario si desea salir, si o no “S/N”, 
si el usuario teclea la letra S el programa se detendrá, de lo contrario continuará ejecutándose."""

# bandera : es una variable que cambia de esta y el ciclo se detiene 
bandera = input("ingrese s/n: ")
while(bandera!= "s"):
    bandera = input("ingrese s/n")
print("Gracias por usar nuestro programa")