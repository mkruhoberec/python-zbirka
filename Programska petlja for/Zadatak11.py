#Napisati program koji će omogućiti unos prirodnog broja n i ispisati djelitelje tog
#broja n

broj = int(input("Unesite broj: "))
broj_ponavljanja = broj
test_djelitelj = 1 #Početni djelitelj kojeg isprobavamo

for i in range(broj_ponavljanja):
    if broj % test_djelitelj == 0:
        print(test_djelitelj, end=' ')
    test_djelitelj += 1