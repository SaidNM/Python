def op(n,m):
	if n == None or m == None:
		return 0
	return n+m 


s1 = "hola"
s2 = "mundo"
lr = map(op,s1,s2)

print (list(lr))

