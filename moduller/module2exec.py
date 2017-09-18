# 1 ile 1000 arasında bir random sayı al, sonra onun karesini al yaz.
# o random sayının bir de karekökünü al, tam sayı mı değil mi kontrol et
from module2randommath import rand,kare
a = rand(0,10)
x = a*a
b = kare(a)
print(a,b)
if type(b) == int:
	print("Tam sayı!")
else:
	print("Tam sayı değil.")

#10.0 dönüyor mesela. float gördüğü için integer demiyor.