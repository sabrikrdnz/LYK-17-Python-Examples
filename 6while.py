#Kullanıcıdan aldığı sayının karesi 1000'den küçükse sayıyı #göster. ve yeni bir sayı almak için sor.
sayi = int(input("Lütfen bir sayi giriniz:"))
while sayi**2 < 1000:
	print(sayi**2)
	sayi = int(input("Lütfen tekrar bir sayı giriniz:"))