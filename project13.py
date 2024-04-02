#DICCIONARIOS EN PYTHON
PEPE = {
"Daniel": "56",
"Anabella": "24",
"Juan": "25"
}
print(PEPE["Daniel"])

PEPE["CARLA"] = "37"
print (PEPE)

del PEPE["CARLA"]

print (PEPE)

print ("Entre la edad de  Juana")
data = input("---->")
PEPE["JUANA"] = data
print (PEPE)

print  ("La Edad de")

print(PEPE.items())

print(PEPE.get("JUANA"))
