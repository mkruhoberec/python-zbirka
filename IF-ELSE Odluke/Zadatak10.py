#Unesite dva broja
#Ispitati sljedeći logički izraz
# broj1 > 0 and broj2 < broj1
#Ako je prethodni izraz ispravan
#Ispisati True te provjeriti sljedeći logički izraz
# broj1 > broj2 and broj2 > 0
#U suprotnom ispisati False
#Ako je prethodni izraz ispravan
#Ispisati True
#U suprotnom False

broj1 = int(input("Unesite prvi broj: "))
broj2 = int(input("Unesite drugi broj: "))

if broj1 > 0 and broj2 < broj1:
    print("broj1 > 0 and broj2 < broj1 = True")
    if broj1 > broj2 or broj2 > 0:
        print("broj1 > broj2 or broj2>broj1 = True")
    else:
        print("False")
else:
    print("False")