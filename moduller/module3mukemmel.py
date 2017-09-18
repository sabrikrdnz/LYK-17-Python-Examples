from random import randint
def mikemmel(sayi):
	mikemmel = []
	for i in range(1,sayi):
		bolenler = []
		for j in range(1,i):
			if i%j == 0:
				mikemmel.append(j)
		if i == sum(bolenler):
			dizi.append(i)
		if len(mikemmel) == 2:
			break
	return mikemmel

def random(x):
	sayi = randint(0,x)
	return sayi

#TAM DEĞİL KONTROL ET! 1,1 dönüyo