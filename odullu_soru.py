liste=[]
isimpuan=[]
naber = {
	'isim':'puan'
	}
sonuc = []
def ogrenci():
	name = input("Adınızı giriniz:")
	isimpuan.append(name)
	x=1
	while x<4:
		point = int(input("Not giriniz:"))
		isimpuan.append(point)
		x+=1
	liste.append(isimpuan)

def hesapla():
	for i in liste:
		for j in i:
			print(i,j)
	#print(naber)


while True:
	cvp = input("Devam etmek istiyor musunuz? e/h > ")
    if cvp=="e":
        ogrenci()
        continue
    elif cvp=="h":
        print(liste)
        hesapla()
    else:
        print("Geçerli parametre gir!")
#daha fazla saçmalama lütfen