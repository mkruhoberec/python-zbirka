from random import randint

niz = []

for i in range(10): #Popunjavanje niza od 10 članova nasumičnim brojevima
    element = randint(0, 100)
    niz.append(element)

print(niz)

for i in range(len(niz) - 1, 0, -1):
    najveci = 0
    for j in range(1, i+1):
        if niz[j] > niz[najveci]:
            najveci = j

    temp = niz[i]
    niz[i] = niz[najveci]
    niz[najveci] = temp

print(niz)