class Slowa:
    def __init__(self,slowo1,slowo2):
        self.slowo1=slowo1
        self.slowo2=slowo2
    def __del__(self):
        print("Obiekt został zniszczony")
    def czy_palindrom(self): 
        odtylu = self.slowo1[::-1] 
        if (self.slowo1 == odtylu): 
            return "Słowo jest Palindromem"
        return "Słowo nie jest Palindromem"
    def czy_metagramy(self):
        wynik = 0
        if self.slowo1 != self.slowo2:
            if len(self.slowo1) == len(self.slowo2):
                for i in range(len(self.slowo1)):
                    for j in range(len(self.slowo2)):
                        if self.slowo1[i] != self.slowo2[j]:
                            wynik+=1
                        i+=1
                    if i>=len(self.slowo2):
                        break
                if wynik>1:
                    return "Słowa nie są Metagramami"
                return "Słowa są Metagramami"
            return "Słowa nie są Metagramami, mają inna długość"
        return "Słowa nie są Metagramami, są takie same"
    def czy_anagramy(self):
        if(sorted(self.slowo1)==sorted(self.slowo2)):
            return "Słowa są Anagramami"
        return "Słowa nie są Anagramami"
def main():
    wyrazy = Slowa("level","leved")
    print(wyrazy.czy_palindrom())
    print(wyrazy.czy_metagramy())
    print(wyrazy.czy_anagramy())
    del wyrazy
if __name__ == "__main__":
    main()