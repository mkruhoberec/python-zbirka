#Deklarirajte niz naziva niz i ograničite ga na 10 elemenata. Napunite niz bez unosa preko
#tipkovnice. Ispišite niz u obrnutom redoslijedu od 10 prema 1..

niz = []
broj_elemenata = 10

for i in range(broj_elemenata):
    element = int(input("Unesite broj: "))
    niz.append(element)

obrnuti_niz = niz[9::-1] #Indeks početnog elementa je 9. Korak je -1.
print(obrnuti_niz)
