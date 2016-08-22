"""
def prueba(f):
	return f()

def enviar():
	return 2+2



print(prueba(enviar))
"""
def seleccion(op):
	def suma(n,m):
		return n+m
	def multiplicacion(n,m):
		return n*m	

	if op == 'suma':
		return suma  #regresa la funcion
	elif op == 'multiplicacion':
		return multiplicacion

fun = seleccion("suma")
print (fun(3,4))

