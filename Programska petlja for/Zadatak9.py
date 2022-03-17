#Unesite neki broj i napravite ispis svih brojeva do tog broja u obrnutom redoslijedu.

max_broj = int(input("Unesi neki broj: "))
broj = max_broj
broj_ponavljanja = max_broj

for i in range(broj_ponavljanja):
    print(broj)
    broj -= 1