#Kullanıcı şarkı adı girsin
#Kullanıcı şarkı süresi girsin.
#Albüm isimleri listelensin
#Kullanıcı listedeki albüm isimlerinden birini seçsin
#Şarkı adı ve şarkı süresi kullanılarak bir şarkı nesnesi oluşturulsun
#Bu şarkı nesnesi için albume_ekle() metodu çağırılsın
#Metodun içinde albümün şarkılar özelliğine bu şarkı eklensin
#Artık yeni şarkı eklenmek istenmediğinde albümler, isimleri ve
#şarkı sayıları ile gösterilsin.

class Album:
    albumler=[]

    def __init__(self,isim,tur):
        self.isim = isim
        self.tur = tur
        self.sarkilar=[]
        Album.albumler.append(self)

    def albume_ekle(self,sarki):
        self.sarkilar.append(sarki)

class Sarki:
    def __init__(self,isim,sure):
        self.isim=isim
        self.sure=sure

album_listesi={"Pop":["Yolla","Kara Kedi"],"Sanat Müziği":["Saklı Kayıtlar","İntizar"]}

for item in album_listesi.items():
    for album_adi in item[1]:
        a=Album(album_adi,item[0])

while True:
    isim=input("Şarkı adı girin: ")
    sure=input("Şarkı süresi giriniz: ")

    print("Albüm Adı"+" | "+ "Albüm Türü")
    for album in Album.albumler:
        print(album.isim)

    secim=input("Şarkıyı eklemek için lütfen albüm adı giriniz: ")
    for album in Album.albumler:
        if album.isim==secim:
            secilen_album=album

    sarki=Sarki(isim,sure)
    secilen_album.albume_ekle(sarki)
    tercih=input("Yeni bir şarkı eklemek ister misiniz? E/H ")
    if tercih !='E':
        break

print("Albüm Adı"+" | "+ "Albüm Türü"+" | "+ "Şarkı sayısı \n")
for album in Album.albumler:
    print(album.isim+" "+album.tur+" "+len(album.sarkilar))