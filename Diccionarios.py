# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 15:33:31 2024

@author: Daniel
"""

#Esto es una prueba

#Diccionarios
my_dict = dict()
my_other_dict = {}
print (type(my_dict))
print (type(my_other_dict))
my_other_dict = {"Nombre": "Daniel", "apellido": "Guerri", "edad": 60}

print (my_other_dict)

my_other_dict = {"Nombre": "Daniel", "apellido": "Guerri", "edad": 60, 1:"Python"}
print (my_other_dict)

my_dict = {
       "Nombre": "Daniel",  #lo que aparece antes de los : es un  indice
       "apellido": "Guerri", 
       "edad": 60,
       "lenguajes":{"Python", "C", "C++"}
       
       }

print (my_dict)
my_dict = {
       "Nombre": "Daniel",  #lo que aparece antes de los : es un  indice
       "apellido": "Guerri", 
       "edad": 60,
       "lenguajes":{"Python", "C", "C++"},
       1:1.75
       }

print (my_dict)

#dentro del diccionario tengo un set que actua cmo ununico valor.

#puedo tener diccionarios adentro de diccionarios.
print(my_dict["Nombre"])  #le pase la clave o el inice y me devolvio el valor de ella

my_dict["Nombre"] = "pepe"

print(my_dict["Nombre"])

my_other_dict ["Calle"] = "pringles"

print (my_other_dict)

del my_dict ["Nombre"]

print (my_dict)

print ("apellido" in my_dict)   #Solo me dice que la clave existe.
print ("apelido" in my_dict)

print (my_dict.items())
print(my_dict.keys())
print(my_dict.values())
My_new_dict = {}
My_new_dict.fromkeys(("Nombre", "Grado"))  #Crea un diccionario vacio solo los indices

My_new_dict ["Nombre"] = "Juana"  #Le agrega un valor a un indice

print(My_new_dict)

My_new_dict ["Nombre"] = "Juana", "Pepe", "Ana"
print(My_new_dict)

My_new_dict ["Nombre"] = input("--->")
print(My_new_dict)

My_new_dict = dict.fromkeys(my_dict)  #le pase las claves de un diccionario a otro
print(My_new_dict)


