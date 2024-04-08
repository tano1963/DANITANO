# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 09:20:12 2024

@author: Daniel
"""

class persona:
        def __init__(self, diccionario1):
            self.diccionario1 = diccionario1
            print (diccionario1)
            diccionario2 = {}
            diccionario2 ={"apellido": "Guerri"}
            print (diccionario1, diccionario2)
            
           
#persona = persona() NO VA !!!!!
diccionario1 = {}
diccionario1 = {"Nombre": "Daniel"}   
mi_persona = persona(diccionario1)       