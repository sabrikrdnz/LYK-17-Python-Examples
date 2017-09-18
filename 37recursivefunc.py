def fucktoriyel(x):
	if x == 1:
		return 1
	else:
		return x*fucktoriyel(x-1)
print("5!:",fucktoriyel(5))
print("8!:",fucktoriyel(8))
print("9!:",fucktoriyel(9))