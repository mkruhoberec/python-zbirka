#Kreirajte funkciju za unos niza, kvadriranje i ispisa kvadrata vrijednosti niza.

def unos():
    niz = []
    broj_clanova = int(input("Unesi broj članova niza: "))
    for i in range(broj_clanova):
        niz.append(int(input("Unesite broj: ")))
    return niz

def kvadrat(x):
    return x**2

def ispis(niz):
    for i in range(len(niz)):
        niz[i] = kvadrat(niz[i])
        print(niz[i], end=" ")

niz = unos()

ispis(niz)