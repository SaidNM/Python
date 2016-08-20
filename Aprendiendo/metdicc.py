d = {
	"rede_sociales": ["Twitter", "FB","Snap"],
	1: "uno",
	"Hola": "Salut"
}

print (d.items()) #muestra las tuplas de las llaves

print(d.keys()) #lista con las claves del diccionario

print(d.values()) #lista con los valores

print (d)
print (d.pop(4,-1)) #diccionario.pop(valor,d) valor en d va a ser lo que regrese en caso de que la clave no se encuentre

print (d)

del d[1] # elimina valor del diccionario

print (d)

d.clear() # borra todos los valores del diccionario

print (d)

d["clave"] = 23 #agrega elementos

print (d)

d2 = d.copy()

print (d2)

