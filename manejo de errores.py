# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 17:18:50 2024

@author: Daniel
"""

#Manejo de Ecepciones (errores)
numberone = 1
numbertwo = 5
numbertwo = "1"

#print(numberone +  numbertwo)  #esto sabemos ue esta mal

# una forma a mano de controalr este error es +

if type (numbertwo) == int:
    print(numberone +  numbertwo)
else:
    print("No se cumplio la condicion ejemplo A")

 

try: 
    print(numberone +  numbertwo)
    print("no se ha producido un error")
    
except:
    print ("Se ha producido un error Ejemplo B")
    
#try Exept else

try: 
    print(numberone +  numbertwo)
    print("no se ha producido un error Ejemplo C")
    
except:
    print ("Se ha producido un error C")
    
else:
    print ("La ejecucion continua correctamente Ejemplo C") #Esta lines solo se ejecuta si no hay errores
    


try: 
    print(numberone +  numbertwo)
    print("no se ha producido un error Ejemplo C")
    
except:
    print ("Se ha producido un error C")
    
else:
    print ("La ejecucion continua correctame")
    
finally:
    
    print ("Esto siempre se ejecuta")
    
    
    
#Captura de Errores por typo o cualquier otra cosa 

 
try: 
        print(numberone +  numbertwo)
        print("no se ha producido un error Ejemplo C")
        
except ValueError:
        print ("Se ha producido un error C por Valor")
        
except TypeError:
        print ("Se ha producido un error C por typo")
    
#Captura de la info del error 

try: 
        print(numberone +  numbertwo)
        print("no se ha producido un error Ejemplo C")
        
except ValueError:
        print ("Se ha producido un error C por Valor")
        
except TypeError as error:
        print ("Se ha producido un error C por typo")
        print (error)
    
    
    
    