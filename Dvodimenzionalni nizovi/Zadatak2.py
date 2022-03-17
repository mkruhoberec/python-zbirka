#Napraviti unos redaka i stupaca matrice preko tipkovnice.

m = int(input("Broj redaka: "))
n = int(input("Broj stupaca: "))

matrica = []

for i in range(m):
    matrica.append([])
    for j in range(n):
        matrica[i].append(j)

print(matrica)