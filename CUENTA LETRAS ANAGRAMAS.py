# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 17:19:00 2024

@author: Daniel
"""
 #Ingreso el String1

def cuentaletras(string1: str ):

    #Cuento las letras del string 1 y guardo el valor
    index1 =0
    for  i in string1:
        index1= index1+1
    return index1

def cuentaletras2 (string2: str):
    #Cuento las letras del string 2 y guardo el valor
    index2 =0
    for  j in string2:
        index2 = index2+1
    return index2
def comparolascadenas (string1: str, string2: str):
    set1 = set (string1)
    set2 = set (string2)
    if set1 == set2:
        print ("Ambos strings tienen las mismas letras pueden formar un anagrama")
   
    else:
        print ("Ambos strings no tienen las mismas letras no podrian formar un anagrama") 
        
        
#MAIN        
        
 #Ingreso el String1  
string1 =  input("---->>>Ingrese el string1:")
 #Ingreso el String2
string2 =  input("---->Ingrese el string2:")


index1= cuentaletras(string1)
index2= cuentaletras2(string2)

if index1 == index2:
    print ("es posible que tengamos un anagrama por que ambos strigs tienen la misma longitud")
    print(index1)
    print(index2)
    Verdadero = comparolascadenas(string1, string2)
        
else:
    print ("Ambos textos tienen distintas cantidades de letras no pueden formar un anagrama")
        
   
    #Comparo el Valor 1 y el Valor 2 
    #Si son iguales puede haber un anagrama 
    #Si no son iguales ya no es un anagrama.
    
#comparacion de Strings

    
