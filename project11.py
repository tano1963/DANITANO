Empleados = []
nombre = "0"
Inscriptos = 0
while  nombre != "quit":
	print ("Entre su numbre y apellido")
	nombre = input("---> ")
	Empleados.append(nombre)
else:
	Empleados.remove("quit")
	print  (Empleados)

Inscriptos = len(Empleados)
print (Inscriptos)
