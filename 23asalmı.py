def asal():
	sayi = int(input("Bir sayi giriniz:"))
	asal = True
	for deger in range(2,sayi):
		if sayi%deger == 0:
			asal = False
			break
	return asal

print(asal())