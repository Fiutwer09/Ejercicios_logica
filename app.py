"""
Aplicacion que provee al usuario una interfaz al usuario  para ejecutar operaciones basicas entre dos numeros
Autor : Jhojan camilo gonzalez cardona 
Fecha: Octubre 6 de 2023 
"""
#crear varibles 
#pedimos l opcion para saber que oprecion va ahacer el usuario
opcion = input ("para sumar ingrese 1,  para restar ingrese 2, para multiplcar ingrese 3, para dividir ingrese 4: ")
#pedimos los numeros 
numero1= int(input ("Ingrese numero 1: "))
numero2= int(input ("Ingrese numero 2: "))

#si la opcion es 1..... Sumamos
if opcion=="1":
    operacion = numero1 + numero2

#si la opcion es 2..... Restamos
if opcion=="2":
    operacion = numero1 - numero2
    
#si la opcion es 3..... Multiplicamos
if opcion=="3":
    operacion = numero1 * numero2

#si la opcion es 4..... Dividimos
if opcion=="4":
    operacion = numero1 / numero2
    
print ("resultado de la operacion es: " + str(operacion))
    
    
