#Deklarirati funkcije unosa i ispisa elemenata jednodimenzionalnog niza

def unos():
    niz = []
    broj_clanova = int(input("Unesi broj članova niza: "))
    for i in range(broj_clanova):
        niz.append(int(input("Unesite broj: ")))
    return niz

def ispis(niz):
    for i in range(len(niz)):
        print(niz[i], end=" ")

niz1 = unos()

ispis(niz1)