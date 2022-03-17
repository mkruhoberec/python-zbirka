#Deklarirajte niz naziva niz i ograničite ga na 10 elemenata. Napunite niz bez unosa preko
#tipkovnice. Pomnožite svaki element niza brojem 3.

niz = []
broj_elemenata = 10

for i in range(broj_elemenata):
    element = int(input("Unesite broj: "))
    niz.append(element)
    
for i in range(broj_elemenata):
    umnozak = niz[i] * 3
    print(umnozak, end=" ")