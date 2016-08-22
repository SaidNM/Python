l = [1,2,3,4]
ll = ["h","o","l","e"]

#l2 = (c * num for c in ll 
#				for num in l)

#for letra in l2:
#	print (letra)

def factorial(n):  #al ser un objeto generados se utiliza la palabra yield en ves de return
	i = 1
	while n > 1:
		i = n*i
		yield i
		n -= 1

for e in factorial(5):
	print (e)
