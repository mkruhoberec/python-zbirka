#Napišite program koji ispisuje zbroj parnih brojeva od 1 do 20

broj = 2 #Prvi parni broj
broj_ponavljanja = int(20/2) #"/" u pythonu daje decimalni broj kao rezultat, for petlja prihvaća samo cijeli.
zbroj = 0 #Početna vrijednost zbroja

for i in range(broj_ponavljanja):
    zbroj += broj #Zbroju dodamo broj
    print("Nakon broja", broj, "zbroj je", zbroj)
    broj += 2 