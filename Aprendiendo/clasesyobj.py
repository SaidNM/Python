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
	def estudiarcaso(self,caso):
		print ('Estudiar caso de ', caso)


pedro = Ingsistemas()
raul = Licderecho(24)


pedro.hablar('Hola soy Pedro')
raul.hablar('Hola pedro, soy Raul')

pedro.programar('Python')
raul.estudiarcaso('Pedro')

"""
print ('Soy pedro y tengo ', pedro.edad)
print ('Soy raul y tengo ',raul.edad)
"""

