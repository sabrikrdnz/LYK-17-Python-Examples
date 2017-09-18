dizi = []
def fib():
	a, b = 1, 1
	while len(dizi) < 10:
		dizi.append(a)
		a,b=b, a + b
	return dizi