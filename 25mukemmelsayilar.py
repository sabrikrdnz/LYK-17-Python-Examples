dizi = []
for i in range(1,1000):
	bolenler = []
	for j in range(1,i):
		if i%j == 0:
			bolenler.append(j)
	if i == sum(bolenler):
		dizi.append(i)
print(dizi)

