while True:
	x = input("sayi gir:")
	if not x:
		break
	try:
		print(float(x)**2)
	except BaseException as e:
		print("girdiğin şey nasıl bişey:",str(e))