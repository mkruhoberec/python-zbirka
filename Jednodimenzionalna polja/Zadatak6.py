#Deklarirajte niz naziva niz i ograničite ga na 10 elemenata. Napunite unosom preko
#tipkovnice. Zbrojite elemente nizova i ispišite njihvo zbroj.

niz = []
broj_elemenata = 10

zbroj = 0

for i in range(broj_elemenata):
    element = int(input("Unesite broj: "))
    niz.append(element)

for i in range(broj_elemenata):
    zbroj += niz[i]

print("Zbroj svih elemenata je", zbroj)