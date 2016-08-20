class Humano:
	def __init__(self,edad):
		self.edad = edad


	def hablar(self,mensaje):
		print (self.edad)
		print (mensaje)



pedro = Humano(26)
raul = Humano(25)

pedro.hablar('Hola')
raul.hablar('Hola pedro')
print ('Soy pedro y tengo ', pedro.edad)
print ('Soy raul y tengo ',raul.edad)


