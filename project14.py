dicc = {}
i = "1"
nombre = "0"
while  i == "1":
	print ("Entre el nombre:")
	nombre = input("---->")
	if nombre == "quit":
		print  (dicc)
		break
	elif nombre != "quit":
		print ("Entre la edad:")
		edad = input("---->")
		dicc.update({nombre:edad})

file1 = open('myfile.txt', 'w') 
file1.writelines(str(dicc)) 
file1.close() 
