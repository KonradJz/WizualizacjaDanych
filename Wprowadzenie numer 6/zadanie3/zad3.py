import numpy as np 
def c(n):
    stop = n*n
    a = np.array([np.arange(1,stop)])
    return a
print(c(5))