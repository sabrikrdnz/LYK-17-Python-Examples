f = open("28bilgileryaz.txt","a")
f.write("Sabri Karadeniz\n")
f.write("26\n")
f.write("Sivas\n")
f.write("1991\n")
f.write("Cumhuriyet Üniversitesi\n")
f.close()

with open("bilgiler.txt","r") as dosya:
	icerik = dosya.readlines()
for satir in icerik:
	print(satir)