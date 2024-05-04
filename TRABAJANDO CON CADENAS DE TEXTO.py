# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 19:21:00 2024

@author: Daniel
"""

word = "Python"
print (word[-1])
print (word[0:2])
print (word[0])
print (word[2:4])
print (word[3:6])

##
print (word + "J")
print ([word[0] + "J"])

#

print (len (word))

#

numeros = [1,2,3,4,5,6,7,8,9,]   #Esto es una lista
print (numeros[0])
print (numeros[1+3])

#
print(word[0:] +"J")

numero10 = [10]
nuevacadena = numeros + numero10
print (nuevacadena)

#quiero ver si a una cadena de nuemeros le puedo sumar un texto
word1 = ["Pyton"]
cadenatextonumero = numeros + word1
print (cadenatextonumero)
#Expresado como una lista si se puede hacer
