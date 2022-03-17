#Potrebno je kreirati 4 funkcije koje će omogućiti zbrajanje, oduzimanje, množenje i
#dijeljenje. Unose brojeva omogućite unutar funkcija. Unutar funkcije se mora izvršiti
#određena operacija i ispisati rezultat iste. Izbornik izraditi pomoću while petlje.


def zbrajanje():
    broj1 = int(input("Unesi prvi broj: "))
    broj2 = int(input("Unesi drugi broj: "))
    zbroj = broj1 + broj2
    print("Rezultat zbrajanja je:", zbroj)

def oduzimanje():
    broj1 = int(input("Unesi prvi broj: "))
    broj2 = int(input("Unesi drugi broj: "))
    razlika = broj1 - broj2
    print("Rezultat oduzimanja je:", razlika)

def mnozenje():
    broj1 = int(input("Unesi prvi broj: "))
    broj2 = int(input("Unesi drugi broj: "))
    umnozak = broj1 * broj2
    print("Rezultat zbrajanja je:", umnozak)

def djeljenje():
    broj1 = int(input("Unesi prvi broj: "))
    broj2 = int(input("Unesi drugi broj: "))
    kolicnik = broj1 / broj2
    print("Rezultat zbrajanja je:", kolicnik)

print("Dobrodošli u kalkulator...")
run = True

while run:
    print("Izaberite operaciju: \n1) Zbrajanje \n2) Oduzimanje \n3) Množenje \n4) Djeljenje \n5) Izlazak iz programa")
    izbor = int(input("Izbor: "))

    if izbor == 1:
        zbrajanje()
    elif izbor == 2:
        oduzimanje()
    elif izbor == 3:
        mnozenje()
    elif izbor == 4:
        djeljenje()
    elif izbor == 5:
        print("Izlazak iz kalkulatora...")
        run = False
    else:
        print("Nije izabrana dobra operacija. Molim upisati: 1, 2, 3, 4 ili 5.")

