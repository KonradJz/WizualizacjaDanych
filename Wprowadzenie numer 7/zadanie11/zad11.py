import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
b = a.reshape((3,4))
print(b)
c = a.reshape((4,3))
print(c)
d = a.reshape((2,6))
print(d)

for i in b.flat:
   print(i)
print('\n')
for i in c.flat:
   print(i)
print('\n')
for i in d.flat:
   print(i)
#po spłaszczeniu wszystkie macierze są identyczne