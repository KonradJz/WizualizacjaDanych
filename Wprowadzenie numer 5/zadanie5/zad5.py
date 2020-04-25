class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)

class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        # lub
        # super().__init__(imie, nazwisko)
        self.pensja = pensja

    def przedstaw_sie(self):
        return "{} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)

class Menadzer(Pracownik):

    def przedstaw_sie(self):
        return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


janusz = Pracownik("janusz", "nowak", 2000)
marcin = Menadzer("marcin", "kowalski", 12000)
adam = Osoba("adam", "malczynski")

print(janusz.przedstaw_sie())
print(marcin.przedstaw_sie())
print(adam.przedstaw_sie())

print(isinstance(janusz , Osoba))
print(isinstance(marcin, Osoba))
print(isinstance(janusz , Menadzer))
print(isinstance(marcin, Menadzer))
print(isinstance(janusz, Pracownik))
print(isinstance(marcin, Pracownik))
print(isinstance(adam, Osoba))
print(isinstance(adam, Menadzer))
print(isinstance(adam, Pracownik))

print(issubclass(Pracownik,Osoba))
print(issubclass(Menadzer,Osoba))
print(issubclass(Osoba,Pracownik))
print(issubclass(Menadzer,Pracownik))