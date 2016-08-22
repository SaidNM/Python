def decorador (funcion):
	def funcioonDec(*args,**kwargs):
		print ("Funcion ejecutada",funcion.__name__)
		funcion(*args,**kwargs)

	return funcioonDec

@decorador
def resta(n,m):
	print (n-m)

#DECORANDO

resta(5,3)
#decorador(resta)(5,3)
