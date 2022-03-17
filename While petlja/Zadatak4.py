#Program treba omogućiti korisniku odabir jedne od četiri aritmetičke operacije (+,-,*,/)
#Svakoj operaciji je potrebno dodijeliti neki broj (npr. 1. Zbrajanje, 2. Oduzimanje, 3.
#Mnozenje, 4. Dijeljenje, 5. Izlaz iz programa) Kada korisnik odabere jednu od navedenih
#operacija, od njega se traži da unese dva broja. Ispisati rezultat odabrane operacije


run = True

while run:
    izbor = input("Unesi željenu operaciju(+, -, /, *)\nZa izlazak upiši 0: ")
    if "+" in izbor:
        print("Izabrano zbrajanje (+)")
        broj1 = float(input("Unesi prvi broj: "))
        broj2 = float(input("Unesi drugi broj: "))
        zbroj = broj1 + broj2
        print("Zbroj je", zbroj)
    elif "-" in izbor:
        print("Izabrano oduzimanje (-)")
        broj1 = float(input("Unesi prvi broj: "))
        broj2 = float(input("Unesi drugi broj: "))
        razlika = broj1 - broj2
        print("Razlika je", razlika)
    elif "*" in izbor:
        print("Izabrano množenje (*)")
        broj1 = float(input("Unesi prvi broj: "))
        broj2 = float(input("Unesi drugi broj: "))
        umnozak = broj1 * broj2
        print("Umnozak je", umnozak)
    elif "/" in izbor:
        print("Izabrano djeljenje (/)")
        broj1 = float(input("Unesi prvi broj: "))
        broj2 = float(input("Unesi drugi broj: "))
        kolicnik = broj1 / broj2
        print("Količnik je", kolicnik)
    elif "0" in izbor:
        print("Izlazak iz kalkukatora...")
        run = False
    else:
        print("Nije izabrana dobra operacija,\nMolim upisati: /,*,- ili +.")
