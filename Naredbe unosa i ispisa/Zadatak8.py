#Unesite dva broja i izračunajte njihovu sumu, razliku, količnik, umnožak
#Sumu ispisati u binarnom sustavu
#Razliku ispisati u heksadekadskom sustavu
#Umnožak ispisati u oktalnom sustavu
#Količnik ispisati u dekadskom sustavu

broj1 = float(input("Unesite prvi broj: "))
broj2 = float(input("Unesite drugi broj: "))

zbroj = broj1 + broj2
razlika = broj1 - broj2
umnozak = broj1 * broj2
kolicnik = broj1 / broj2

print("Zbroj je", bin(int(zbroj))) #bin() prima samo cijele brojeve. Zbroj pretvaramo u cijeli broj prije pretvaranja u binarni. Nije najtočnije rješenje.
print("Razlika je", hex(int(razlika))) #hex() prima samo cijele brojeve. Zbroj pretvaramo u cijeli broj prije pretvaranja u binarni. Nije najtočnije rješenje.
print("Umnožak je", oct(int(umnozak))) #oct() prima samo cijele brojeve. Zbroj pretvaramo u cijeli broj prije pretvaranja u binarni. Nije najtočnije rješenje.
print("Količnik je", kolicnik)