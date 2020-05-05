import pandas as pd
import numpy as np
import xlrd
import openpyxl

xlsx = pd.ExcelFile('zadanie1\imiona.xlsx')
df = pd.read_excel(xlsx)
print("PODPUNKT A")
print(df[df['Liczba']>1000])

print("PODPUNKT B")
print(df[df['Imie']=="KONRAD"])

print("PODPUNKT C")
print(df.agg({'Liczba':['sum']}))

print("PODPUNKT D")
zakres = (df[((df.Rok>2000) & (df.Rok < 2005))])
print(zakres.agg({'Liczba':['sum']}))

print("PODPUNKT E")
m = (df[df['Plec']=="M"])
print(m.agg({'Liczba':['sum']}))
k = (df[df['Plec']=="K"])
print(k.agg({'Liczba':['sum']}))

print("PODPUNKT F")
imiona = df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec'])
for index, group in enumerate(imiona, start=1):
    print(f"{index} {group[0]}")
    print(f"{group[1].iloc[0]['Imie']}", end=' ')
    print(f"{group[1].iloc[0]['Liczba']}")

print("PODPUNKT G")
k = (df[((df.Plec=='K'))].sort_values(by="Liczba"))
m = (df[((df.Plec=='M'))].sort_values(by="Liczba"))
print(k.tail(1))
print(m.tail(1))