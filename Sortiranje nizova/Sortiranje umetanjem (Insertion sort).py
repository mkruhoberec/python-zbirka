from random import randint

niz = []

for i in range(10): #Popunjavanje niza od 10 članova nasumičnim brojevima
    element = randint(0, 100)
    niz.append(element)

print(niz)

for i in range(len(niz)):
    trenutna_vrijednost = niz[i]
    pozicija = i
    
    while pozicija > 0 and niz[pozicija - 1] > trenutna_vrijednost:
        niz[pozicija] = niz[pozicija - 1]
        pozicija = pozicija - 1
        niz[pozicija] = trenutna_vrijednost
    
print(niz)