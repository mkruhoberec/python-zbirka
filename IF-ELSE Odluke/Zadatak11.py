#Napisati program za množenje dva broja u rasponu zaključno s brojem 10.
#Na početku programa upitati korisnika želi li množiti brojeve. Ukoliko odgovori pozitivno s da
#omogućiti unos i množenje. Ukoliko odgovori negativno, omogućiti izlazak iz programa

izbor = input("Želite li množiti brojeve: da/ne ")

if izbor == "da" or izbor == "DA":
    broj1 = int(input("Unesite broj između 1 i 10: "))
    if broj1 <= 10:
        broj2 = int(input("Unesite broj između 1 i 10: "))
        if broj2 <= 10:
            umnozak = broj1 * broj2
            print("Umnožak je", umnozak)
        else:
            print("Broj mora biti između 1 i 10.")
    else:
        print("Broj mora biti između 1 i 10.")
else:
    print("Izlazak iz programa.")