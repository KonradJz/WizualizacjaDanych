class Ciagi:
    def __init__(self):
        self.a1=0
        self.a2=0
        self.a3=0
    def wyswietl_dane(self):
        return self.a1,self.a2,self.a3
    def pobierz_elementy(self,a1,a2,a3):
        self.a1=a1
        self.a2=a2
        self.a3=a3
        return self.a1,self.a2,self.a3
    def pobierz_parametry(self,x1,r,n):
        self.x1=x1
        self.r=r
        self.n=n
        return self.x1,self.r,self.n
    def policz_sume(self):
        return ((( 2 * self.x1 + (self.n-1) * self.r ) / 2 ) * self.n )
    def policz_elementy(self):
        liczby = 0
        if(self.x1==self.n):
            return 1
        for i in range(self.x1,self.n,self.r):
            liczby+=1
        return liczby
def main():
    ciag = Ciagi()
    print(ciag.wyswietl_dane())
    print(ciag.pobierz_elementy(18,19,20))
    ciag.pobierz_parametry(10,3,30)
    print(ciag.policz_sume())
    print(ciag.policz_elementy())
if __name__ == "__main__":
    main()