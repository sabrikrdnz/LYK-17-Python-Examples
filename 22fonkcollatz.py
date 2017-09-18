#n sayısı çiftse n = n/2 , tekse n = 3*n+1 olsun ve fonksiyon kendi kendini
# n==1 olana kadar tekrar etsin.

def collatz():
	num = int(input("Sayi gir:"))
	dizi = []
	while num != 1:
		if num%2==0:
			num = num/2
			dizi.append(num)
		else:
			num = 3*num + 1
			dizi.append(num)
	return dizi
print(collatz())