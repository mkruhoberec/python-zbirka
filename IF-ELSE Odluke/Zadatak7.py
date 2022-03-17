#Unesite broj. Ako je unesen broj 1 omogući operaciju zbrajanja dva broja i ispiši zbroj.
#Unosom bilo kojeg drugog broja omogući operaciju množenja dva broja i ispiši umnožak

izbor = int(input("Za zbrajanja odaberite 1. \nZa množenje bilo što drugo : "))

if izbor == 1:
    broj1 = int(input("Unesite prvi broj: "))
    broj2 = int(input("Unesite drugi broj: "))
    zbroj = broj1 + broj2 
    print("Zbroj:", zbroj)
else:
    broj1 = int(input("Unesite prvi broj: "))
    broj2 = int(input("Unesite drugi broj: "))
    umnozak = broj1 * broj2
    print("Umnožak:", umnozak)