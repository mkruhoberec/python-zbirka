#Deklarirajte niz naziva niz i ograničite ga na 10 elemenata. Omogućite unos elemenata preko
#tipkovnice. Ispišite neparne elemente niza

niz = []
broj_elemenata = 10

for i in range(broj_elemenata):
    element = int(input("Unesite broj: "))
    niz.append(element)

neparni_elementi = niz[::2] #Ovako je u skripti napravljeno. AKo želimo samo parne ELEMENTE treba upisati niz[::2]
print(neparni_elementi)