import numpy as np 
slowa = ['marcin','uihqke','csłqwe','hweawe','akzcat']
s =[[],[],[],[],[]]
#marcin 1 linjka, miła po ukosie, mucha 1 kolumna, taczka od tylu ostatni wiersz
for i in range(0,5,1):
    s[i] = np.array(list(slowa[i]))
    s[i] = np.fromiter(slowa[i], dtype='U1')
    print(s[i])