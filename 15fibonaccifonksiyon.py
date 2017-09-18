def fib(n):
	results = []
	a, b = 1, 1
	while a<n:
		results.append(a)
		a,b=b, a + b
	return results

	if len(results) < 81:
	print(results[80])

print(fib(7000000))

