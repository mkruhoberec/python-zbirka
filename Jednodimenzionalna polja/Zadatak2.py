#Deklarirajte niz naziva niz i ograničite ga na 10 elemenata. Omogućite unos elemenata preko
#tipkovnice. Ispišite samo parne elemente niza.

niz = []
broj_elemenata = 10

for i in range(broj_elemenata):
    element = int(input("Unesite broj: "))
    niz.append(element)

for i in range(broj_elemenata):
    if i % 2 == 1:
        print(niz[i], end=" ") 

#Alternativno rješenje

svaki_drugi = niz[1::2] #list[start:stop:step] #Ovako je u skripti napravljeno. AKo želimo samo parne ELEMENTE treba upisati niz[::2]
print(svaki_drugi)

for i in range(len(svaki_drugi)):  #Ako se baš želi svaki broj ispisati posebno
    print(svaki_drugi[i], end=" ")