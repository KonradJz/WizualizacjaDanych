import numpy as np
def dodawanie(m1, m2):
    a = np.sin(m1)
    b = np.cos(m2)
    return a+b
m1 = np.array([[np.pi/4,np.pi/2,np.pi/3],[7*np.pi/6,np.pi/6,5*np.pi/6]])
m2 = np.array([[0,np.pi/4,np.pi/3],[7*np.pi/6,np.pi/6,5*np.pi/6]])
print( dodawanie(m1,m2) )