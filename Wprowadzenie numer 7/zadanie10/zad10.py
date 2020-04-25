import numpy as np
a = np.array([[1,2,3,4,5,6,7,8,9],[1,1,1,1,1,1,1,1,1],[2,2,2,2,2,2,2,2,2],[3,3,3,3,3,3,3,3,3],[4,4,4,4,4,4,4,4,4],[5,5,5,5,5,5,5,5,5],[6,6,6,6,6,6,6,6,6],[7,7,7,7,7,7,7,7,7],[8,8,8,8,8,8,8,8,8]])
print(a)
b = a.reshape((27,3))
print(b)
#27x3, 81x1, 9x9, 3x27, 1x81 Mamy tylko takie możliwości ponieważ jest tylko 81 miejsc w macieży i trzeba mnożyć tak, aby wszystkie miejsca były zapełnione