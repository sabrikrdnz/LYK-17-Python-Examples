#27dosya.txt dosyasına yazıyoruz.
f = open("27dosya.txt","r")

r = f.read(20)
print(r)
print("*"*10)

r = f.read(30)
print(r)
print("*"*10)

print(f.readline(1))
print(f.readlines())

print("*"*10)

with open("27dosya.txt","r") as dosya:
	icerik = dosya.readline()
	print(icerik)

print("*"*10)

f = open("27dosya.txt","a")
f.write("Bu bir dosya mıdır?")
f.write("Evet bu bir dosyadır.")
f.close()

f = open("27dosya.txt","r")
print(f)