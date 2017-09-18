def add(x,y):
	return x+y
print(add(2,6))

def shout(phrase = 'Yihhuuuu!'):
	print(phrase)
shout('AHEYYY') #Hiçbirşey yazmazsak yihhu yazar
				#Bir değerle çağırırsak onu döner OVERRIDE


def echo(text, prefix=''):
	print('%s%s' % (prefix, text))
echo('kuzey','güney')