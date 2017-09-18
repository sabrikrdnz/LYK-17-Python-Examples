# 2000 ile 3000 arasındaki 5 ve 7 ile bölünebilen sayıları stringe çevirip yaz.
dizi = []
for x in range(2000,3001):
	if x%5==0 and x%7==0:
		dizi.append(str(x))
print(dizi)