# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 14:50:31 2024

@author: Daniel
"""
global spam
def scopetest(pepe):
    spam = pepe
    return print (spam)
    
scopetest("Global")

print("")


def scopetest(pepe, numero):
    spamm = pepe
    x = numero +10
    return print (spamm, x)
    
scopetest("Globalllllll", 10)

print ("")

def scopetest(pepe, numero1, numero2):
    spamm = pepe
    x = numero1 +10
    y = numero2
    return print (spamm, x, y )
    
scopetest("Globalllllll", 10, 30)