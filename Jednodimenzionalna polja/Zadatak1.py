#Deklarirajte niz naziva niz i ograničite ga na 10 elemenata. Omogućite unos elemenata preko
#tipkovnice. Ispišite elemente niza

niz = []
broj_elemenata = 10

for i in range(broj_elemenata):
    element = int(input("Unesite broj: "))
    niz.append(element)

for i in range(broj_elemenata):
    print(niz[i], end=" ")