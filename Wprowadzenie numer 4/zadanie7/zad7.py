class Robaczek:
    def __init__(self):
        self.x=0
        self.y=0
        self.krok=1
    def idz_w_gore(self,ile_krokow):
        self.y += ile_krokow * self.krok
        return self.y 
    def idz_w_dol(self,ile_krokow):
        self.y -= ile_krokow * self.krok
        return self.y
    def idz_w_lewo(self,ile_krokow):
        self.x -= ile_krokow * self.krok
        return self.x
    def idz_w_prawo(self,ile_krokow):
        self.x += ile_krokow * self.krok
        return self.x
    def pokaz_gdzie_jestes(self):
        return self.x, self.y

def main():
    pozycja = Robaczek()
    pozycja.idz_w_gore(35)
    pozycja.idz_w_prawo(15)
    pozycja.idz_w_dol(65)
    pozycja.idz_w_lewo(13)
    print(pozycja.pokaz_gdzie_jestes())
if __name__ == "__main__":
    main()