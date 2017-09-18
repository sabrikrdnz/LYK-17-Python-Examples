#9x9 tahtadaki verilen bir koordinatın nerede olduğunu bulan fonksiyon.
#Öncelikle 9 kare içerisinde arama yapsın, daha sonra o kare içerisinde arama yapsın.
def sudoku():
	x = int(input("x'i giriniz:"))
	y = int(input("y'yi giriniz:"))

	a = x/3
	b = y/3

	z = x%3
	t = y%3

	print("(%s,%s) içerisinde (%s,%s)" %(a, b, z, t))