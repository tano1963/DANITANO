# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:38:40 2024

@author: Daniel
"""

#Loops

#While
my_condicion =0

while my_condicion <10:
    print(my_condicion)
    my_condicion += 1
    
else:
    print ("mi condicion es mayor que 10")
print ("Termine")

while my_condicion < 20:
  my_condicion += 1 
  if my_condicion == 15:
      print ("micondicion es 15")
      break
      print ("mi condicion")
      
print ("la ejecucion continua")

#For

my_list =[35, 24, 23,33,44,55,66]

for element in my_list: 
    print (element)

my_tuple = (1, 2,3, 4, 5,6 )
print (my_tuple)

my_set = {"Hola", "Chau"}
print (my_set)

my_dict = {"Nombre": "Daniel", "sobrenombre": "osvaldo", "apellido": "guerri"}
print(my_dict.values())
print(my_dict.keys())

print ("entre en el for")

for element in my_dict.keys():
    if element == "sobrenombre":
        break  #esto me saca del for que incluye al else
    print (element)
    
else:
    print ("el bucle for ha terminado")
    
    
    
    
    






