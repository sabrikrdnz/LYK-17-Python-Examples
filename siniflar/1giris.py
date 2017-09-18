class Kurs:
	adi = "PHP"
	vantilator = 1

	def araver(self):
		print(self.adi+" sınıfı ara veriyor")
	
	def vantilatorlazimmi(self):
		return self.vantilator < 2
		
php = Kurs() #Kurs sınıfından php adında bir nesne türettik.
#print(php.adi) #Ürettiğimiz sınıftan bir özellik yazdırdık.
php.araver()
php.vantilator=1
python = Kurs()
python.adi = "Python" 
python.vantilator = 0
python.araver()
#print(python.adi)
#print(python.vantilator) #Kurs sınıfından ürettiğimiz python
						 #nesnesinin vantilator özelliğini aldık.
while python.vantilatorlazimmi():
	print(str(python.vantilator)+" yetmez "+str(python.vantilator+1)+" olsun")
	python.vantilator += 1