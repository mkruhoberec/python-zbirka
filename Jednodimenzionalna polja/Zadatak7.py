#Deklarirajte niz naziva niz i ograničite ga na 10 elemenata. Napunite niz bez unosa preko
#tipkovnice. Ispišite sumu parnih elemenata niza.

niz = []
broj_elemenata = 10

zbroj = 0

for i in range(broj_elemenata):
    element = int(input("Unesite broj: "))
    niz.append(element)

parni_elementi = niz[1::2] #Ovako je u skripti napravljeno. AKo želimo samo parne ELEMENTE treba upisati niz[::2]

for i in range(len(parni_elementi)):
    zbroj += parni_elementi[i]

print("Zbroj parnih elemenata je", zbroj)