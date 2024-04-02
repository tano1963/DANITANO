# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 18:02:26 2024

@author: Daniel
"""

class Pepe:
    pass   #Para que la clase no haga nada 

class Persona:
    def __init__(self,nombre, apellido): #Este es el contructor de la clase
        self.nombre = nombre
        self.apellido = apellido
    
my_person = Persona("danie", "guerri")

print(f"{my_person.nombre} {my_person.apellido}")

#veamos funciones definidas dentro de la clase

class Persona:
    def __init__(self,nombre, apellido): 
        self.full_name = ("daniel" "guerri" )
    def caminar (self):
        print (f"{self.full_name} Esta Caminando") #Esta funcion pertenece a la clase y uso variables definidas dentro de la clase
        
mi_persona = Persona("daniel", "guerri")
print(mi_persona.caminar)
   
mi_persona.caminar()  
mi_persona.full_name = "PePe"   
print (mi_persona.full_name)


        
        
        