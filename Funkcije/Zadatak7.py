#Kreirati funkcije koje će omogućiti unos elemenata niza, ispis elemenata niza, obrnuti ispis
#elemenata te ispis samo parnih vrijednosti. Napravite izbornik za korisnika upotrebom
#while petlje

def unos():
    niz = []
    broj_clanova = int(input("Unesi broj članova niza: "))
    for i in range(broj_clanova):
        niz.append(int(input("Unesite broj: ")))
    return niz

def ispis(niz):
    for i in range(len(niz)):
        print(niz[i], end=" ")
    print("\n---------")

def obrnuti_ispis(niz):
    for i in range(len(niz)):
        pozicija = len(niz) - 1 - i
        print(niz[pozicija], end=" ")
    print("\n---------")

def parni_clanovi(niz):
    for i in range(len(niz)):
        if i % 2 == 0:
            print(niz[i], end=" ")
    print("\n---------")

run = True
niz = []

while run:
    print("Za unos podataka izaberite: 1.")
    print("Za ispis izaberite: 2.")
    print("Za obrnuti ispis izaberite: 3.")
    print("Za ispis parnih elemenata izaberite: 4.")
    print("Za izlazak iz programa izaberite: 5.")

    izbor = int(input("Izbor: "))
    
    if izbor == 1:
        niz = unos()
    elif izbor == 2:
        ispis(niz)
    elif izbor == 3:
        obrnuti_ispis(niz)
    elif izbor == 4:
        parni_clanovi(niz)
    elif izbor == 5:
        print("Izlazak iz programa...")
        run = False
    else:
        print("Nije unesen dobar izbor. Upisati: 1, 2, 3, 4 ili 5.")
