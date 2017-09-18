"""
Otomobil(marka,model,yil,renk,fiyat,durumu)
Mosotiklet(aynı şeyler)
10 tane motosiklet 10 tane otomobil nesnesi tanımla.
Kullanıcı girdiğinde soralım
Kiralamak istediği araç türü
Eğer otomobil kiralamak istiyosa otomobilleri, motosiklet istiyosa
motosikletleri listele
Listelendikten sonra bir araç seçsin, ardından kaç gün kiralamak
istediğini sor. 
Kiraladığı aracın bilgilerini ve ödeyeceği toplam parayı görsün.
Sonra o aracın uygun olup olmadığını görsün
Bu araç artık kiralanamaz olsun ve tekrar araç kiralamak istediğinde o araç
listede görünmesin.

"""

class Otomobil:
	def __init__(self,marka,model,renk,fiyat,durum):
		self.marka = marka
		self.model = model
		self.renk = renk
		self.fiyat = fiyat
		self.durum = True

	def otomobil_ekle(self,marka,model,renk,fiyat,durum):
		self.marka = marka
		self.model = model
		self.renk = renk
		self.fiyat = fiyat
		self.durum = True

class Motosiklet:
	def __init__(self,marka,model,renk,fiyat,durum):
		self.marka = marka
		self.model = model
		self.renk = renk
		self.fiyat = fiyat
		self.durum = True

	def motosiklet_ekle(self,marka,model,renk,fiyat,durum):
		self.marka = marka
		self.model = model
		self.renk = renk
		self.fiyat = fiyat
		self.durum = True
