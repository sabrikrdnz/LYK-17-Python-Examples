f = open("35.txt","w")
while True:
	isim = input("Öğrencinin ismi:")
	f.write(isim)
	for i in range(3):
		grade = int(input("Notu giriniz:"))
		f.write("," + str(grade))
	f.write("\n")
	devamkosulu = input("Tamam mı devam mı? E/h")
	if not devamkosulu == "e":
		break