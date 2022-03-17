#Napraviti fiksni unos stupaca i redaka.

matrica = []

for i in range(3):
    matrica.append([])
    for j in range(3):
        matrica[i].append(i+j)

print(matrica)