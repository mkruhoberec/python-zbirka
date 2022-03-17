#Kreirati dvije matrice s fiksnim elementima i zbrojiti ih.
from random import randint

m = int(input("Broj redaka: "))
n = int(input("Broj stupaca: "))

matrica1 = []
matrica2 = []

for i in range(m):
    matrica2.append([])
    matrica1.append([])
    for j in range(n):
        matrica1[i].append(randint(0, 10))
        matrica2[i].append(randint(0, 10))

print(matrica1)
print(matrica2)

zbroj_matrica = []

for i in range(m):
    zbroj_matrica.append([])
    for j in range(n):
        zbroj_matrica[i].append(matrica1[i][j] + matrica2[i][j])

print(zbroj_matrica)