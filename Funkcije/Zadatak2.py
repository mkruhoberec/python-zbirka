#Napišite funkcije za zbrajanje dva broja i pozovite je u glavnom dijelu programa. Omogućite
#izvršavanje te funkcije 3 puta

def zbroj():
    broj1 = int(input("Unesi prvi broj: "))
    broj2 = int(input("Unesi drugi broj: "))
    zbroj = broj1 + broj2
    print("Zbroj brojeva", broj1, "i", broj2, "je", zbroj)

for i in range(3):
    zbroj()
    print("-------------------")