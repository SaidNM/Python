class Humano:
	def __init__(self,edad):
		self.edad = edad


	def hablar(self,mensaje):
		print (mensaje)

class Ingsistemas(Humano):
	def __init__(self): #sobreescriir metodo de edad, solamente en la clase Ing en sistemas
		print ('Hola')
	def programar(self,lenguaje):
		print ('Voy a programar en ', lenguaje)

class Licderecho(Humano):
	def __init__(self,escuela):
		print('Lic. en derecho egresado de: ', escuela)

	def estudiarcaso(self,caso):
		print ('Estudiar caso de ', caso)

class Estudioso(Licderecho,Ingsistemas): # se tomara el metodo init de la primera clase que aparezca en la herencia
	pass

pepe = Estudioso('IPN')
pepe.hablar('Hola soy de herencia multiple')
pepe.programar('Java')
pepe.estudiarcaso('Juanito')


