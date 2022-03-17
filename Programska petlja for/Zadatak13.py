#Nastavnik ispituje učenike na satu
#Ispitivati će svakog n-tog učenika u imeniku
#Napisati program koji će omogućiti unos broja učenika te prirodan broj n kao
#kriterij odabira učenika iz imenika
#Program treba ispisivati redne brojeve učenika koje će nastavnik ispisivati. 

broj_ucenika = int(input("Unesi broj učenika: "))
kriterij = int(input("Unesi koji svaki učenik se ispituje: "))
ispitani_ucenik = 1 #Početni ispitani učenik

broj_ponavljanja = round(broj_ucenika / kriterij) #Zaokružujemo prema gore

for i in range(broj_ponavljanja):
    print("Ispisuje se učenik s rednim brojem:", ispitani_ucenik)
    ispitani_ucenik += kriterij