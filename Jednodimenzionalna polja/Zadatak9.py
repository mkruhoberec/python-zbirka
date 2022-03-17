#Deklarirajte niz naziva niz i ograničite ga na 10 elemenata. Napunite niz bez unosa preko
#tipkovnice. Izvršite kvadriranje – operacija u pythonu je a**2.

niz = []
broj_elemenata = 10

for i in range(broj_elemenata):
    element = int(input("Unesite broj: "))
    niz.append(element)
    
for i in range(broj_elemenata):
    kvadrat = niz[i] ** 2
    print(kvadrat, end=" ")
