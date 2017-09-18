while True:
	x = input("sayi gir:")
	if not x:
		break
	try:
		print(float(x)**2)
	except:
		print("girdigin sayi sayi degil müdür")