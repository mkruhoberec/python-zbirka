max_broj = int(input("Unesi broj: "))

broj_ponavljanja = int(max_broj / 2)
broj = 2 

for i in range(broj_ponavljanja):
    print(broj)
    broj += 2

#Alternativno rješenje
max_broj = int(input("Unesi broj: "))

broj_ponavljanja = max_broj
broj = 1

for i in range(broj_ponavljanja):
    if broj % 2 == 0:
        print(broj)
    broj += 1