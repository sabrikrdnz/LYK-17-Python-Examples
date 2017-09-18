#29fibonacci.txt ye 1000'e kadar olan fibonacci sayılarını yaz.
a, b = 1, 1
yaz = open("29fibonacci.txt","w")
while a<1000:
	yaz.write(str(a) +'\n')
	a,b=b, a + b

for fib in open("fibonacci.txt","r"):
	print(fib)