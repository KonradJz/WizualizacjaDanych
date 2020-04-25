import numpy as np 
def diag(n):
    a = np.array([i for i in range(n,0,-1)])
    mat_diag = np.diag([a for a in range(n,0,-1)])
    print( mat_diag)
diag(15)
