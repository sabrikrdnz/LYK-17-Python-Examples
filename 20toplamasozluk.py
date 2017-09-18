#girilen 4 sayıdan ilk ikisini bir son ikisini bir toplayıp bu değerleri çarpan fonk.
def islem():
	sozluk = {}
	for i in range(4):
			num = int(input("Sayi giriniz:"))
			sozluk[str(i)] = num
	carpim = (sozluk["0"]+sozluk["1"])*(sozluk["2"]+sozluk["3"])
	return carpim

print(islem())