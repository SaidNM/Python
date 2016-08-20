s = ","
t = ("H","o","l","a")
print (len(s)) #tamaño de la cadena
print (s.count( " ")) # parametros cadena.count(valor,inicio,fin), este metodo busca un caracter en especifico
print (s.lower()) # convierte la cadena en minusculas
print (s.upper()) #convierte la cadena en mayusculas
print(s.replace("o","3")) #cadena.replace(valor,nuevovalor,repeticiones), Cambion un elemnto de la cadena por otro
print (s.split("o",3)) # cadena.split(separador,maxsplit)  , divide la cadena cadaque encuentre el caracter
#si utilizamos s.split('') tomara valores nulos
print (s.find('a')) #cadena.find(valor, inicio,fin), busca un caracter en una cadena y devuelve la posicion
#para obtener la ultima ocurrencia se utiliza s.rfind

print (s.join(t)) #junta cada uno de los caracteres por en una cadena, separandolo por el simbolo dado en la cadena
