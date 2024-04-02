# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 15:33:36 2024

@author: Daniel
"""

#SETS#

my_set =set()
my_other_set = {}  #Esto es un diccionario

print (type(my_set))

print (type(my_other_set))

my_other_set = {"Danie", "Guerri", 60}

print (my_other_set)

print (len (my_other_set))
my_other_set.add("Tano")
print (my_other_set)


#Un set no es una estructura ordenada metio tano donde quiso

#Un Set no admite repeticiones 
#Un set no respecta orden si lo ejecuto de nuevo me implrime en otro orden
 
print ("Tano" in my_other_set)
print ("Tani" in my_other_set)

my_other_set.clear()    #El clear borro todos los elementos 
print (len(my_other_set))

del my_other_set   #Lo destruyo

my_set = {"Danie", "Guerri", 60}

my_list = list(my_set)

print (my_list)
print (my_list[0])

my_other_set ={"Carla", "denise", "mochi"}
my_new_set = my_set.union(my_other_set)
print (my_new_set)

print (my_new_set. union ({"Java", "C#"}))

print (my_new_set.difference(my_set))






