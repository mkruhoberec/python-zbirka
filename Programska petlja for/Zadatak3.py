#Ispiši prvih šest brojeva u obrnutom nizu. Npr. 1,2,3,4,5,6 ispisati kao 6,5,4,3,2,1.

broj = 6 #Početna vrijednost broja
broj_ponavljanja = 6 

for i in range(broj_ponavljanja):
    print(broj)
    broj -= 1 #U svakom koraku broj smanjimo za 1