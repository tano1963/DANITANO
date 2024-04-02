# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 10:13:57 2024

@author: Daniel
"""

### List comprhension ###
my_original_list = [0,1,2,3,4,5,6]
print (my_original_list)
my_list = list (i for i in my_original_list)
print(my_list)

my_list = list (i for i in range(3))
print(my_list)

my_range = range(0,7)
print(my_range)