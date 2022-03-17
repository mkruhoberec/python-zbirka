#Ispisati samo parne brojeve brojevnog niza od prvih 10 brojeva.

broj = 0 #Početna vrijednost - prvi parni broj
broj_ponavljanja = 5 #U prvih 10 brojeva ima 5 parnih

for i in range(broj_ponavljanja):
    print(broj)
    broj += 2 #U svakom koraku broj povećamo za 2