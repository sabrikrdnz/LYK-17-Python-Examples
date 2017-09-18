# 10 kisiden adı soyadı bölümü okulu bilgilerini alan ve ekrana 
# bilgileri basan en optimize kodu yaz.
def function():
	kisilist = []
	for i in range(1):
		kisiler = {
			'isim': 'isim',
			'soyad': 'soyad',
			'bolum': 'bolum',
			'okul': 'okul'
		}

		isim = input("Lütfen isminizi giriniz:")
		soyad = input("Lütfen soyadınızı giriniz:")
		bolum = input("Lütfen bölümünüzü giriniz:")
		okul = input("Lütfen okulunuzu giriniz:")

		kisiler.update({'isim':isim,'soyad':soyad,'bolum':bolum,'okul':okul})

		for key, value in kisiler.items():
			x=[key,value]
			kisilist.append(x)
		kisilist.append("\n")
	print(kisilist)
function()

#BİTMEDİ