#Cree un programa que calcule el promedio de tres notas para n estudiantes.
estudiantes= input("Escriba su nombre: ")
nota1=float(input("Ingrese su primer nota: "))
nota2=float(input("Ingrese su segunda nota: "))
nota3=float(input("Ingrese su tercer nota: "))
prom = nota1+nota2+nota3
for i in range (2):
    print("El promedio de estos esrudiantes  son: " + str(prom/3))