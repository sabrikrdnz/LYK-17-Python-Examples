def fakt(x):
	toplam = 1
	for i in range(1,x+1):
		toplam = toplam*i
	print(toplam)	

fakt(x = int(input("Bir sayi gir:")))