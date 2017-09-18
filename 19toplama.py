#girilen 4 sayıdan ilk ikisini bir son ikisini bir toplayıp bu değerleri çarpan fonk.
def ornek():
	i = 0
	toplam1 = 0
	toplam2 = 0
	carpim = 0
	while i < 4:
		sayi = int(input("Bir sayi giriniz:"))
		if i < 2:
			toplam1 += sayi
			i += 1
		else:
			toplam2 += sayi
			i += 1
	carpim = toplam1*toplam2
	return carpim
print(ornek())
