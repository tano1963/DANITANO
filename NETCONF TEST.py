# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 10:02:39 2024

@author: Daniel
"""

import xmltodict
import json



data_email = "<email><para>Mary</para><de>daniel</de><contenido>Hola Mary</contenido></email>"
print ("Datos originales")
print (data_email) 

#esto convierte al XML en un Diccionario
print ("") 
to_dicc = xmltodict.parse(data_email)
print (to_dicc)

json_email = json.loads(json.dumps(to_dicc))

print (json_email)

print ("presentar los formatos con formato JSON")

for k,v in json_email.items():
    print(k + ":" + str(v) + "\n")  # no se por que no funciona el new line
    
xml_email = xmltodict.unparse(json_email)
print (xml_email)

import xml.etree.ElementTree as et

contenedor = et.fromstring (data_email)

for x in contenedor :
    print (x.tag+ ":" +x.text)


print ("")

datafrutas = """
<frutas>
    <manzana>
        <Color>Roja</Color>
        <sabor>Deliciosa</sabor>
    </manzana>
    <platano>
        <Color>Amarillo</Color>
        <sabor>neutro</sabor>
    </platano>
</frutas>
"""
print (datafrutas)

to_dicc2 = xmltodict.parse(datafrutas)
print (to_dicc2)  #Aqui lo imprimo como un diccionario

print("")

print (to_dicc2["frutas"])




print ("Aqui comienzo")

#Accede a los elementos de frutas
frutas = to_dicc2["frutas"]

print(frutas)

print("")

for fruta, detalle in frutas.items():
    color = detalle["Color"]
    print(f"Color de {fruta}: {color}")
    
    
print("")


print ("Continuacion Vidio 2")











