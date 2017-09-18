import os
dizin = input("Dizin?")

def listele(path):
	dosyalar = os.listdir(path)

	for dosya in dosyalar:
		print(dosya)
		if os.path.isdir(os.path.join(path,dosya)):
			listele(dosya)
		listele(os.path.join(path,dosya)

listele(dizin)