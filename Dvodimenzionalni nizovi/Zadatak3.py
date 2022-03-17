#Omogućiti tipkovnički unos redaka i stupaca te elemenata matrice.

m = int(input("Broj redaka: "))
n = int(input("Broj stupaca: "))

matrica = []

for i in range(m):
    matrica.append([])
    for j in range(n):
        element = int(input("Unesi element matrice"))
        matrica[i].append(element)

print(matrica)