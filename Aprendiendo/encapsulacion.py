# __ atributo privado
class prueba(object):
	def __init__(self):
		self.__privado = "Soy privado"
		self.publico = "Soy publico"

	def __metodprivado(self):
		return 'soy privado'

	def metodopublico(self):
		return "soy publico"

	def getprivado(self):
		return self.__privado
	def setprivado(self,valor):
		self.__privado = self.__metodprivado()

# metodo para acceder a privados

obj = prueba()

#print (obj.publico)
#print (obj.__privado)
#obj.metodopublico()
#obj.getprivado()


#darle un valor a una parte privada
obj.setprivado("Tengo un nuevo valor")
# imprimir metodo privado
print (obj.getprivado())
