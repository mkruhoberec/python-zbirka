#Unesite prvih 10 brojeva, ali izuzmite broj 7.

broj = 1 #Početna vrijednost broja
broj_ponavljanja = 10

for i in range(broj_ponavljanja):
    if broj != 7: #Broj ispisujemo samo ako je različit od 7
        print(broj)
    broj += 1 #U svakom koraku broj povećamo za jedan