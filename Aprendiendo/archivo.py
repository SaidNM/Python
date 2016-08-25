"""
try:
	f =open("ejemplo.txt","r") #abrir archivo
#modo "r", debe existir un archivo
#modo "w", si no existe el archivo se crea
#modo "a", agrega elento a un archivo, debe de existir el archivo
#modo "r+", lectura y escritura, debe existir el archivo
except:
	f="Error al abrir el archivo"

print (f)	
"""
"""
f =open("ejemplo.txt","r+")
print (f)
f.close()
"""
try:
	f = open('ejemplo.txt','w')
except:
	exit()
#f.write("Hola estoy creando mi primer ")
#f.seek(10)
#print (f.tell()) # no siempre es correcto el valor 
#f.write("intruso")
agregar = ["hola\n","\t0","\t1"]
#f.writelines(agregar)
f.close()

if not f.closed:
	f.writelines(agregar)

	
""" 	Agregar mas caracteres al archivo
try:
	f=f=open("ejemplo.txt","a")
except:
	exit()
f.write("archivo en python")
f.close()

"""






