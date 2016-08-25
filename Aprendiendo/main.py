"""
import modulo #importar un modulo desde la misma ubicacion

print (modulo)
e = modulo.Ejemplo() #definir objeto
e.imprime()			#imprimir

modulo.fejemplo()#utilizar una funcion del modulo
"""
from modulo import Ejemplo # solo importa la clase ejemplo
							# para importar todo se escribe *


e = Ejemplo()
e.imprime()

#para importar de un paquete usamos import paquete_carpeta.nombre_modulo
									#para utilizar funcion se utiliza paquete_nombre.nombremodulo.funcion()
								



