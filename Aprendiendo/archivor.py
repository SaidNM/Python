try:
	f=open('ejemplo.txt','r')
except:
	exit()

#print(f.read()) #argumento opcional, el numero de bytes a leer
"""
while True:
	print (f.readline()) #se detiene hastaun caracter de espacio
	if f.readline() == "": # se detiene en caracter vacio
		break
"""


lineas = f.readlines()
print (lineas)

#imprime todas las lineas
for l in lineas:
	print ("=>",l,'\n\n')
