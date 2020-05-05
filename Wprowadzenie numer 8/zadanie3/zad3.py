import numpy as np 
import pandas as pd


df = pd.read_csv('zadanie3/zamowienia.csv',sep=";")

print("PODPUNKT A")
print(df["Sprzedawca"].unique())

print("PODPUNKT B")
print(df.sort_values(by="Utarg").tail(5))

print("PODPUNKT C")
print(df.groupby(["Sprzedawca"]).agg({"idZamowienia":['count']}))

print("PODPUNKT D")
print(df.groupby(["Kraj"]).agg({"idZamowienia":['count']}))

print("PODPUNKT E")
sum=(df[((df.Kraj == "Polska") & (df.DataZamowienia>"2004-12-31") & (df.DataZamowienia<"2006-01-01"))].agg({"idZamowienia":['count']}))
print(sum)

print("PODPUNKT F")
avg=(df[((df.DataZamowienia>"2003-12-31") & (df.DataZamowienia<"2005-01-01"))].agg({"Utarg":['average']}))
print(avg)

print("PODPUNKT G")
plik2 = open("zadanie3/zamowienia_2004.csv","w+")
plik2.write(str(avg))
plik2.close()
plik = open("zadanie3/zamowienia_2005.csv","w+")
plik.write(str(sum))
plik.close()