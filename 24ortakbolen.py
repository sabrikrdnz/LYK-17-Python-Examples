def ortakbolen():
	sayi1 = int(input("İlk sayı :"))
	sayi2 = int(input("İkinci sayı :"))
	dizi = []

	enbyk = 0
	enkck = 0

	if sayi1 > sayi2:
		enbyk = sayi1
		enkck = sayi2
	else:
		enbyk = sayi2
		enkck = sayi1

	for i in range(1,enkck):
		if enbyk % i == 0 and enkck % i == 0:
			dizi.append(i)
	return dizi

print(ortakbolen())
