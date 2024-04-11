# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 09:20:12 2024

@author: Daniel
"""

class persona:
        def __init__(self, diccionario1, edad):
            self.diccionario1 = diccionario1
            self.edad = edad
            print (diccionario1)
            diccionario2 = {}
            diccionario2 ={"apellido": "Guerri", "Edad": edad}
            print (diccionario1, diccionario2)
            
           

diccionario1 = {}
diccionario1 = {"Nombre": "Daniel"}  
edad =61
mi_edad= persona(diccionario1, edad) #aca es pomo que la llamo a la clase

print (type(mi_edad))

print("")
"""
class edad:   
    def __init__(self, edad):
        self.edad = edad
        print (edad)


mi_edade = edad(60)
"""