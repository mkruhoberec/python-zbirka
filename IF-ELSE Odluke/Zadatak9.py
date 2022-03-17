#Unesite dva broja
#Ispitati sljedeći logički izraz
#broj1 > 0 and broj2 < a
#Ako je prethodni izraz ispravan
#Ispisati True u suprotnom ispisati False.

broj1 = bool(input("Unesite 0 ili 1: "))
broj2 = bool(input("Unesite 0 ili 1: "))

if broj1 > 0 and broj2 < broj1:
    print("True")
else:
    print("False")