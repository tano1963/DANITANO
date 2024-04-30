# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 17:19:00 2024

@author: Daniel
"""
 #Ingreso el String1

def cuentaletras(string1: str, string2: str ):

    #Cuento las letras del string 1 y guardo el valor
    index1 =0
    for  i in string1:
        index1= index1+1
    return index1
    
    #Cuento las letras del string 2 y guardo el valor
    index2 =0
    for  j in string2:
        index2 = index2+1
    return index2
    
 #Ingreso el String1  
string1 =  input("---->>Ingrese el string1:")
 #Ingreso el String2
string2 =  input("---->Ingrese el string2:")


index1= cuentaletras(string1, string2)
index2= cuentaletras(string1, string2)
print(index1)
print(index2)
   
    #Comparo el Valor 1 y el Valor 2 
    #Si son iguales puede haber un anagrama 
    #Si no son iguales ya no es un anagrama.
    


