import numpy as np

A = np.array([[n+m*10 for n in range(5)] for m in range(5)])
v1 = np.arange(0, 5)

#print(np.dot(A, A)) #array uzerinden matris carpimi
#print(np.dot(A, v1)) #alingment üzerinden matris carpimi

M = np.matrix(A)
v = np.matrix(v1).T
print(A*A)
print(M*v)