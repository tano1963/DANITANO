# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:22:00 2024

@author: Daniel
"""

### Fechas###
from datetime import datetime

now =datetime.now()

print (now.year)

print (now.month)

print (now.day)

print (now.hour)

print (now.minute)

print (now.second)

timestamp = now.timestamp()

print (timestamp)



year_2025 = datetime(2025, 1,1)
print (year_2025)


from datetime import time

current_time  =time (3,4,5)

print (current_time)

from datetime import date

current_date = date(2022,1,1)
print (current_date)

current_date = date.today()
print (current_date)








