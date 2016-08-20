l = [1,"Dos",5]

buscar = 5
print (buscar in l) #buscar elementos en una lista, devuelve true, false
if buscar in l:
	print (l.index(buscar))
else:
	print('El elemento no esta en lista')

print(l)

l.append("Nuevo") #agregar elementos a la lista
print(l)

print (l.count(1)) #numero de veces que se encuentra el elemento

l.insert(2,"New") #insertar en la posicion 2 lista.insert(indice,elemento)
print (l)

iterable = [1,5,"f"]
l.extend(iterable) #transforma la lista y agrega elementos
print (l)

l.pop() #saca y elimina un elemento de una lista
l.remove(1) # remueve la primer ocurencia con el valor dado
print (l)

l.reverse() #invierte los elementos de la lista

print (l)