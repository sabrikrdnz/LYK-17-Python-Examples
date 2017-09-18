from numpy import random

r1 = random.rand(5) # 0 - 1 aralığında decimal bir değer üretiyo.
r2 = random.rand(4,5) # 4 e 5 lik bir matris şeklinde 0-1 arasında değer
r3 = random.random_integers(0,10) # random 1 adet integer üretir 0-10 arasında

print(r2)