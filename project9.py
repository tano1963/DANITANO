import sys
from sys import argv

number = int(raw_input("> "))
sitios_visitados = []
for i in range(number):
	lugares = raw_input("> ")
	sitios_visitados.append(lugares)
print (sitios_visitados)
