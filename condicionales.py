"""progtrama que muestra el manejo de condicionales 
en python 3
octubre 20/10/2023"""

#pedimos nombre, si nombre es Maria la saludamos 
nombre = input("ingrese nombre: ")
if nombre =="maria":
    print ("Hola Maria")
    
else: 
    print("Usted no es maria")

print ("------elif------") #manera de separar condicionles 

estrato = int(input("Ingrese estrato: "))
if estrato == 1:
    print("usted tiene derecho a subsidio completo ")
elif estrato == 2: #condicion internedia, de lo contrario, es una contracion. 
    print("usted tiene derecho a medio subsidio ")
else:
    print("usted no tiene derecho a subsidio ")
