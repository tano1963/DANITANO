dicc{}
while nombre != "quit":
	print "Entre el nombre:"
	nombre = raw_input("---->")
	print "Entre la edad:"
	edad = raw_input("---->")
	dicc.update({nombre:edad})
else:
	print dicc
