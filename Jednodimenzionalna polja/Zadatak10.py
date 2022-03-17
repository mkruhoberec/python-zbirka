#Kreirajte dva niza od po 5 elemenata. Zatim napunite prvi niz preko tipkovnice. Nakon toga
#premjestite elemente prvog niza u drugi kreirani niz i ispišite taj niz.

niz1 = []
niz2 = []
broj_elemenata = 5

print("Unesite članove prvog niza.")
for i in range(broj_elemenata):
    element = int(input("Unesite broj: "))
    niz1.append(element)

print("Unesite članove drugog niza.")
for i in range(broj_elemenata):
    element = int(input("Unesite broj: "))
    niz2.append(element)

for i in range(broj_elemenata):
    niz2[i] = niz1[i]

print(niz2)