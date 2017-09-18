#f(x) = x**3 - 3x**2 + x - 2

def fonksiyon():
	x = int(input("Lütfen bir sayi giriniz:"))
	sonuc = (x**3) - 3*(x**2) + x -2
	return sonuc

print(fonksiyon())