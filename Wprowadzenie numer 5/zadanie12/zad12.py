def Miesiace():
    Miesiace = ["Styczeń","Luty","Marzec","Kwiecień","Maj","Czerwiec","Lipiec","Sierpień","Wrzesień","Październik","Listopad","Grudzień"]
    for i in Miesiace:
        yield i
def main():
    Miesiace = Miesiace()
    for i in range(12):
        print(next(Miesiace))
if __name__ == "__main__":
    main()