#Preko tipkovnice unesite množitelj matrice s fiksno određenim elementima.
from random import randint

m = int(input("Broj redaka: "))
n = int(input("Broj stupaca: "))

skalar = int(input("Unesite skalar kojim množimo: "))

matrica = []

for i in range(m):
    matrica.append([])
    for j in range(n):
        matrica[i].append(randint(0,10))

rezultat = []

for i in range(m):
    rezultat.append([])
    for j in range(n):
        rezultat[i].append(matrica[i][j] * skalar)

print(matrica)
print(rezultat)