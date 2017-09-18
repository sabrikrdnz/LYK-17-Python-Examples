#Ogretmen ve Ogrenci class'ımız var.
# Buna Sınıf ve Şubeyi ekliyoruz.
class Ogrenci:
	def __init__(self, isim, soyisim):
		self.isim = isim
		self.soyisim = soyisim
		self.dersler = []

	def isim_soyisim(self):
		return self.isim + " " + self.soyisim

	def kayit(self,ders):
		self.dersler.append(ders)

class Ogretmen:
	def __init__(self, isim, soyisim):
		self.isim = isim
		self.soyisim = soyisim

	def isim_soyisim(self):
		return self.isim + " " + self.soyisim

class Ders:
	def __init__(self,isim):
		self.isim = isim
				
class Sube:
	def __init__(self, subeadi):
		self.subeadi = subeadi

o_adi = input("Lütfen öğrencinin adını giriniz: ")
o_soyadi = input("Lütfen öğrencinin soyadını giriniz: ")

e_adi = input("Lütfen eğitmenin adını giriniz: ")
e_soyadi = input("Lüfen eğitmenin soyadını giriniz ")

sube_adi = input("Lütfen şube adını giriniz: ")

ogrenci = Ogrenci(o_adi, o_soyadi)
egitmen = Ogretmen(e_adi, e_soyadi)
sube = Sube(sube_adi)
while True:
	ders_adi = input("Almak istediğiniz dersi yazınız: ")
	ders = Ders(ders_adi)
	
	a = input("Başka bir ders almak istiyor musunuz? E/h")
	if a != "e" or a != "E": break

print("Öğrencinin adı: "+ogrenci.isim)
print("Öğrencinin soyadı: "+ogrenci.soyisim)
print("Eğitmenin adı: "+egitmen.isim)
print("Eğitmenin soyadı: "+egitmen.soyisim)
print("Dersin adı: "+ders.isim)
print("Şube adı: "+sube.subeadi.isim)

