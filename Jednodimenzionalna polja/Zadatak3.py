#Deklarirajte niz naziva niz i ograničite ga na 10 elemenata. Omogućite unos elemenata preko
#tipkovnice. Ispišite svaki četvrti element niza.
#Mislim da je u skripti rješeno za svaki 3.

niz = []
broj_elemenata = 10

for i in range(broj_elemenata):
    element = int(input("Unesite broj: "))
    niz.append(element)

svaki_cetvrti = niz[::4]
print(svaki_cetvrti)