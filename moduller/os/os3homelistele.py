#tüm home dosyasını listele ve git onu txt dosyasına kaydet.
import os
f = open("os3homelistele.txt","w")
dizin = os.listdir("/")
for i in dizin:
	f.write("========")
	if os.path.isdir(os.listdir("/"+i)) == True:
		for j in os.path.isdir(os.listdir("/"+i)):
			dosya = os.listdir(j) 
			f.write(j+ "\n")
f.close()