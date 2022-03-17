#Unesite dva broja. Pomnožite ih i zbrojite. Ispišite umnožak i zbroj
#Ako su umnožak i zbroj jednaki ispisati: Umnožak i zbroj su jednaki
#U suprotnom ispisati: Umnožak i zbroj nisu jednaki

broj1 = int(input("Unesite prvi broj: "))
broj2 = int(input("Unesite drugi broj: "))

umnozak = broj1 * broj2
zbroj = broj1 + broj2

print("Umnožak je", umnozak)
print("Zbroj je", zbroj)

if umnozak == zbroj:
    print("Umnožak i zbroj su jednaki.")
else:
    print("Umnožak i zbroj nisu jednaki")
