#Sljedeća matrica m x n treba ispisati elemente koji se nalaze na dijagonali.
from random import randint

m = int(input("Broj redaka: "))
n = int(input("Broj stupaca: "))

matrica = []

for i in range(m):
    matrica.append([])
    for j in range(n):
        matrica[i].append(randint(0, 10))

print(matrica)

for i in range(m):
    for j in range(n):
        if i == j:
            print(matrica[i][j])