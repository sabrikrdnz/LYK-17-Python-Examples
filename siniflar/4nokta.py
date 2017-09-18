class Nokta:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def topla(self):
		return self.x + self.y

p = Nokta(3,4)
print(p.x)
print(p.y)
print(p.topla())