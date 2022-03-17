#Omogućite unos dva broja 0 ili 1.
#Upotrijbite operaciju logičkog I.
#AKo je rezultat TRUE ispišite true
#U suprotnom ispišite False

broj1 = bool(input("Unesite 0 ili 1: "))
broj2 = bool(input("Unesite 0 ili 1: "))

if broj1 == True and broj2 == True:
    print("True")
else:
    print("False")