class NaZakupy:
    def __init__(self,nazwa_produktu,ilosc,jednostka, cena):
        self.nazwa_produktu=nazwa_produktu
        self.ilosc=ilosc
        self.jednostka=jednostka
        self.cena=cena
    def wyswietl_produkt(self):
        return self.nazwa_produktu, self.ilosc, self.jednostka, self.cena
    def ile_produktu(self):
        ile = self.ilosc * 1
        return ile, self.jednostka
    def ile_kosztuje(self):
        ile = self.ilosc * self.cena
        return ile
def main():
    Warzywo = NaZakupy("Cebula",5,"Szt.",2)

    print(Warzywo.wyswietl_produkt())
    print(Warzywo.ile_produktu())
    print(Warzywo.ile_kosztuje())
if __name__ == "__main__":
    main()