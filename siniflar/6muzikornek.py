# Önce albüm class ı oluştur Albüm(isim, tür)
# sonra şarkı class ı oluştur. şarkı(isim,süresi)
#{"pop":["Yolla","Karakedi"],"sanatmüziği:"["saklıkayıtlar,intizar"]}

#kullanıcı öncelikle şarkı eklemek istesin.
#şarkıyı bir albüme dahil etsin.
#albüme her şarkı ekledikten sonra albümdeki şarkıları listelesin
#ve albümteki toplam şarkı sayısını göstersin.
#çıkış yapılınca da tüm albümler şarkıları ile listelensin.

class Album:
	albumler = []
	def __init__(self,isim,tur):
		self.isim = isim
		self.tur = tur
		Album.albumler.append(self) #Her bir album nesnesi yaratıldığında
									#Album.albumler içine album nesnesini
									#ekliyorum

class Sarki:
	def __init__(self,isim,sure):
		self.isim = isim
		self.sure = sure


album_listesi = {"Pop": ["Yolla","Kara Kedi"], "Sanat Müziği": ["Saklı Kayıtlar", "İntizar"]}

for item in album_listesi.items():
	for album_adi in item[1]:
		a = Album(album_adi, item[0])

print("Album Adı" + " | " + "Album Türü")
for album in Album.albumler:
	print(album.isim)