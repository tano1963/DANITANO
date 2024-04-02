#################################################################
# Esto es una lista que contiene multiples listas como elementos
##################################################################

list1 = [["Alpha", "Betha", "Gama"], [1, 2, 3], ["Daniel", "Carla", "Denise"]]

#Es una unica lista con tres listas, Si imprimo la lista

print ("Esta es la lista completa")
for i in list1:
	print (i)
#--------------------------------------------------------------
#Ahora vamos a imprimir cada uno de los elementos de la lista

print  ("Esta es la lista listada por cada uno de los elementos")

for i in list1:
	for x in i:
		print (x)

