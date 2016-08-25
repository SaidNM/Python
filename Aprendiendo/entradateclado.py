try:
	valor = input("Introduce un numero: ") #input() lee el numero de cmd
	valor = int(valor)					#todo numero leido en cmd es de typo string
except:
	print ("Introduce un numero")
else:
	print (valor)
