# -*- coding: utf-8 -*-
"""
Created on Tue May  7 18:16:17 2024

@author: Daniel
"""

### Excepciones ###

try:
    print (5 + "5")
except:
    print ("Dio error")  #Ademas de imprimirlo para la ejecucion
else:  #Esto es opcional
    print ("La ejecucion continuara")  #Salgo por aqui si no se produce un error
    
    
finally: #Esto es opcional
    print ("La ejecucion continuara por el finally") #Si o Si esto se ejecuta
    
#Excepciones por tipo

try:
    print (5 + "5")
except TypeError as error: 
    print ("Dio error de tipo")  #Ademas de imprimirlo para la ejecucion
    print (error)
except Exception as MiExcepcion:
    print (MiExcepcion)