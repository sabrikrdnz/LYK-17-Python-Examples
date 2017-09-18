# Kullanıcıdan istediğimiz sayıya kadar
# tüm sayıların kendisi:karesi şeklinde ekrana basan
# program.

x = int(input("Lütfen bir sayi giriniz:"))
d = {}
for i in range(x):
	d[i] = i**2
print(d)