#deneme dizini 1-2-3-4 dosya. kullanıcıya hangi dosyayı silmesini soruyoz, onu siliyoz.
import os
dosya = os.listdir("deneme") # [1.txt, 2.txt, 3.txt]
x = input("Hangi dizin silinecek:")
for i in dosya: # os.listdir([1.txt, 2.txt, 3.txt])
	os.remove(x+"/"+i)
os.rmdir(x)
