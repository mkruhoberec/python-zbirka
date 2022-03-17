#Unesite dva broja. Ako je zbroj veći od 20 ispišite: Suma je veća od 20.
#U suprotnom ispišite : Suma je manja od 20.

broj1 = int(input("Unesite prvi broj: "))
broj2 = int(input("Unesite drugi broj: "))

zbroj = broj1 + broj2

if zbroj > 20:
    print("Suma je veća od 20.")
else:
    print("Suma je manja od 20.")