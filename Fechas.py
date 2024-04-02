# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 15:35:08 2024

@author: Daniel
"""

#Dates Fechas 

from datetime import datetime

now =datetime.now()

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.second)

timestamp = now.timestamp()

print (timestamp)

year_2024 = datetime(2024, 3, 20, 17,59)

print (year_2024)


from datetime import time
current_time = time(hour=18, minute=29, second=8)  #a Time hay que pasarle parametros

print (current_time.hour)
print (current_time.minute)
print (current_time.second)


current_time = time(hour=18+1, minute=29, second=8)  #puedo sumar

print (current_time.hour)
print (current_time.minute)
print (current_time.second)


from datetime import timedelta
start_timedelta = timedelta(200,100,100, weeks=10)
end_timedelta = timedelta(300,100,100, weeks=13)

print (start_timedelta-end_timedelta)








