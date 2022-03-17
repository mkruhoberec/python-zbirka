#Kreirajte dvije funkcije: funkciju za unos osobnih podataka {oib, ime i prezime, grad} te
#funkciju za unos podataka o školovanju (razred, naziv, smjer, broj predmeta po razredu)
#Rješite problem OIB-a sa if-else uvjetovanjem unutar funkcije. Ako je OIB izvan raspona
#od 10 znakova ispišite poruku o grešci i ponovite unos. Glavni izbornik izradite pomoću
#while petlje.

#Unos osobnih podataka

def osobni_podaci():
    print("Unos osobnih podataka: ")
    print("-----------------------")

    run = True
    while run:
        oib = int(input("Unesite OIB (11 znamenki): "))
        if len(str(oib)) != 11:
            print("Nije uneseno 11 znamenki. \nMolim ponovni unos 11 znamenki: ")
        elif len(str(oib)) == 11:
            run = False
    ime = input("Unesite ime: ")
    prezime = input("Unesite prezime: ")
    grad = input("Unesite grad: ")

def skolski_podaci():
    print("Unos podataka o školovanju: ")
    print("----------------------------")

    razred = int(input("Unesite broj razreda: "))
    naziv = input("Unesite naziv škole: ")
    smjer = input("Unesite smjer školovanja: ")
    predmet = input("Unesite broj predmeta u trenutnom razredu: ")

run = True
while run:
    print("Unos podataka...")
    print("Unos osobnih podataka (1)")
    print("Unos podataka o školovanju (2)")
    print("Izlaz (3)")
    
    izbor = int(input("Unesi odabir: "))

    if izbor == 1:
        osobni_podaci()
    elif izbor == 2:
        skolski_podaci()
    elif izbor == 3:
        run = False
