# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Tuples
my_tuple   = tuple()
my_other_tuple = tuple ()


my_tuple = ( 60, 1.77, "Daniel", "Guerri")
print (my_tuple)

print (my_tuple[0])

print (my_tuple.count ("Daniel"))  #imprime las veces que aparece
print (my_tuple.index ("Daniel"))   #imprime el indice donde aparece

#En las tuplas no se puede cambiar el valor

my_other_tuple = ( 1,2,3,4,5)
print (my_other_tuple)
my_sum_tuple = my_tuple + my_other_tuple  #Sume dos tuplas 
print (my_sum_tuple)

#cambio una tupla a lista 
my_tuple = list (my_tuple)  #converti una tupla en una lista 
print (type (my_tuple))
my_tuple[3] = "Pepe"   #ahora como es una lista le puedo cambiar el valor.

print (my_tuple)
my_tuple.insert(2, "Azul")
print (my_tuple)

my_tuple =tuple(my_tuple)   #La converti de nuevo a tupla
print(type(my_tuple))

del my_tuple  #hice desaparecer la tupla ya no existe no es un clear de los valores 
              #desaparece la tupla
