def ogrenci_ekle():
	name = input("İsim giriniz:")
	count = 0
	grades = []
	grades.append(name)
	while count < 3:
		grade = int(input("Not giriniz:"))
		grades.append(grade)
		count += 1
	return grades

def tercih():
	liste = []
	tercih = "E"
	while tercih == "E":
		liste.append(ogrenci_ekle())
		tercih = input("Devam etmek istiyor musunuz?: (E / H) :")
	return liste
ogrenci_listesi = tercih()

ort = 0.0
def maximum():
	for ogrenci in ogrenci_listesi:
		maximum = 0
		notlar = ogrenci[1:]
		i = 0
		while i < len(notlar):
			if notlar[i] > maximum:
				maximum = notlar[i]
			i += 1
		ogrenci.append(maximum)
	return ogrenci_listesi

def minimum():
	for ogrenci in ogrenci_listesi:
		minimum = ogrenci[4]
		notlar = ogrenci[1:]
		i = 0
		while i < len(notlar):
			if notlar[i] < minimum:
				minimum = notlar[i]
			i += 1
		ogrenci.append(minimum)
	return ogrenci_listesi

def ortalama():
	for ogrenci in ogrenci_listesi:
		notlar = ogrenci[1:4]
		toplam = notlar[0]+notlar[1]+notlar[2]
		ort = toplam / 3
		ogrenci.append(ort)
	return ogrenci_listesi
ogrenci_listesi = maximum()
ogrenci_listesi = minimum()
ogrenci_listesi = ortalama()

print(ogrenci_listesi)









