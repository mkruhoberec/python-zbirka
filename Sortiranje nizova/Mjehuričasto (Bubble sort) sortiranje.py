from random import randint

niz = []

for i in range(10): #Popunjavanje niza od 10 članova nasumičnim brojevima
    element = randint(0, 100)
    niz.append(element)

print(niz)

for i in range(len(niz)):
    for j in range(len(niz) - 1):
        if niz[j] > niz[j+1]:
            temp = niz[j]
            niz[j] = niz[j+1]
            niz[j+1] = temp

print(niz)