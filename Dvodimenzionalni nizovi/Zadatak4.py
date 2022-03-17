#Pomnožiti svaki element matrice s brojem 3

m = int(input("Broj redaka: "))
n = int(input("Broj stupaca: "))

matrica = []
matrica_puta_tri = []

for i in range(m):
    matrica.append([])
    matrica_puta_tri.append([])
    for j in range(n):
        matrica[i].append(i + j)
        matrica_puta_tri[i].append((i + j) * 3)

print(matrica)
print(matrica_puta_tri)