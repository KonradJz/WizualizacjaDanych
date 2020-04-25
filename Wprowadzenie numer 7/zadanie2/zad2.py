import numpy as np
a = np.array( [[5,10,15],[5,10,15],[5,10,15]] )
b = np.array( [[10,15,20],[10,15,20],[10,15,20],[10,15,20]] )
print(a.min(axis=1))
print(a.max(axis=1))
print(b.min(axis=1))
print(b.max(axis=1))
