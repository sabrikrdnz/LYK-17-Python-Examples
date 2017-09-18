# 10 kisiden adı soyadı bölümü okulu bilgilerini alan ve ekrana 
# bilgileri basan en optimize kodu yaz.

def kayit():
	liste=[]
	for i in range(2):
		a=[]
		name = input("ad gir:")
		surname = input("soyad gir:")
		depart = input("bölüm gir:")
		school = input("okul gir:")
		a.append(name)
		a.append(surname)
		a.append(depart)
		a.append(school)
		liste.append(a)
	return liste
ogrenciler = kayit()

def yazdir():
	for i in ogrenciler:
		for j in i:
			print(j[0] + j[1]+ j[2]+ j[3])
yazdir()

#BİTMEDİ