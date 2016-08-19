def mi_funcion(num1,num2): #def nombre_funcion (parametros)
	return (num1+num2)

""" def mi_funcion(num1=0,num2=2):
		print (num1 +num2)
	mi_funcion() 
	
	""" #no existe el error debido a que s einicializan en la definicion, y si recibe parametros estos no cambian su valor por el de la variable inicializada
""" def mi_funcion(cad,num=2, *algomas):
		print (cad * num2)
		for cadena in algomas
			print cadena * num2
	mi_funcion('hola',4,'algomas') 
""" #no importa que reciba valores de mas, estos se mostraran gracias al * se guardara en una tupla

""" def mi_funcion(cad,num2=2, **algomas):
		print (cad * num2)
		print (algomas['cadenaextra'])
	mi_funcion('Hola',5,cadenaextra = 'hola') 

""" #la funcion estara guardando dentro de un diccionario 
a = 3
b =4
resultado = mi_funcion(a,b)
print (resultado)
