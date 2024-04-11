# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 16:58:54 2024

@author: Daniel
"""



"""    
for index in range  (1, 101):
          divisiblepor3 = ((index % 3) == 0)
          diviciblepor5 = (index % 5 == 0)
if (divisiblepor3 and diviciblepor5 ):
    print ("Fizbuzz")
elif divisiblepor3:
    print ("Fizz")
elif diviciblepor5:
    print (index)
    print ("Buzz")
else:
    print(index)
"""    
    
for index in range (1,101):
    if ((index % 3) == 0):
        print(index)
        print ("Es divicible por 3")
    elif ((index % 5) == 0):
        print (index)
        print ("Es divicible por 5")
    else:
        print (index, "no es divisible ni por 3 ni por 5")