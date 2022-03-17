#Deklarirajte niz naziva niz i ograničite ga na 10 elemenata. Napunite unosom preko
#tipkovnice. Kopirajte u drugi niz samo parne elemente prvog niza.

niz = []

broj_elemenata = 10

for i in range(broj_elemenata):
    element = int(input("Unesite broj: "))
    niz.append(element)

samo_parni_niz = niz[1::2] #Ovako je u skripti napravljeno. AKo želimo samo parne ELEMENTE treba upisati niz[::2]
print(samo_parni_niz)
