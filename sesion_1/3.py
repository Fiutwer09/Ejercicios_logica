"""cree un programa que lea el monto de un prestamo y el plazo en meses,
y muestre al usuario el valor de las cuotas pagando un interes fijo 
del 2.7% mesual."""


prestamo = float(input("Ingrese el monto del prestamo: "))
plazo = int(input("Ingrese los meses del plazo: "))
interes = 0.027

porcentaje = interes * prestamo
cuotas = plazo * porcentaje
total = prestamo + cuotas
toltal2 = total / plazo
print ("El valor de su prestamos por " + str(plazo) + " meses, nos da un interes de  " + str(cuotas))
print("El porcentaje de interes por mes es de " + str(porcentaje))
print("El valor de su cuota mensual seria de: " + str(toltal2))
print ("Su total a pagar seria de " + str(total))