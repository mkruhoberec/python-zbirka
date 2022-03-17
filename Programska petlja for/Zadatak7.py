#Unesi neki broj i ispiši sve brojeve do tog broja počevši od 1

max_broj = int(input("Unesi neki broj: "))
broj_ponavljanja = max_broj

broj = 1 #Početna vrijednost ispisa 

for i in range(broj_ponavljanja):
    print(broj)
    broj += 1
