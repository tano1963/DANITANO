# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 18:49:16 2024

@author: Daniel
"""

#Funciones las funciones son recursivas se pueden llamar a si mismo

def my_function ():   #Asi defino una funcion
    print ("Esto es una funcion")


my_function()

def sum_to_values(primero: int, segundo: int ):  #el int es inutil el tipo es dinamico
    print (primero + segundo)

sum_to_values (1,2)
sum_to_values("33", "22")  #Si es vez de sumar dividiria esto daria error
    
def sum_to_values_with_return(primero: int, segundo: int ):  #el int es inutil el tipo es dinamico
   return primero + segundo

resultado = sum_to_values_with_return(10,5)

print (resultado)

#Lo mismo

def sum_to_values_with_return(primero: int, segundo: int ):  #el int es inutil el tipo es dinamico
   resultado = primero + segundo
   return resultado

sum_to_values_with_return(10,5)

print (resultado)

def imprime_nombre(nombre, apellido):
    print (apellido, nombre)

imprime_nombre ("guerri", "daniel")

#otra funcion que invierte los parametros que le paso no lo entendi
def imprime_nombre(nombre, apellido):
    print (f"{nombre}, {apellido}")

imprime_nombre (apellido = "guerri", nombre = "Daniel")

def imprime_nombre_withdefault(nombre, apellido, alias = "sin alias"):
    print (f"{nombre}, {apellido}, {alias}")


imprime_nombre_withdefault("Daniel", "guerri")
imprime_nombre_withdefault("Daniel", "guerri", "tano")


def suma_de_dos_valores (val1, val2):
    return (val1+val2)

resultado = suma_de_dos_valores(3,4)

print (resultado)
print ( suma_de_dos_valores(3,4))

def print_apellido(nombre, apellido):
    print (f"{nombre}, {apellido}")
    
print_apellido("daniel", "guerri")

print_apellido(apellido = "guerri", nombre= "daniel")   # no se por que no lo da vuelta

#a las funciones se les pueden pasar cosas por defecto
def print_apellido(nombre, apellido, alias = "sin alias"):
    print (f"{nombre}, {apellido}")

print ("daniel", "guerri")  #por mas que debia pasarle un dato mas y no se lo pase como esta 
#definido como alias no importa si lo paso o no

#supongamos que quiero pasarle muchos paramentros

def print_text(*text):
    print(text)
    
print_text("Hola", "danie,", "guerri")

print_text("Hola", "danie,", 1)


    
    
    

