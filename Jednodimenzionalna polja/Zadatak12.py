#Napunite niz s 10 elemenata i ispišite najveći i najmanji element niza.(MIN/MAX)

niz = []

broj_elemenata = 10

for i in range(broj_elemenata):
    element = int(input("Unesite broj: "))
    niz.append(element)

najmanji = najveći = niz[0]

for i in range(len(niz)):
    if najmanji > niz[i]:
        najmanji = niz[i]
    elif najveći < niz[i]:
        najveći = niz[i]
    
print("Najmanji element niza:", najmanji)
print("Najveći element niza:", najveći)

#alternativno rješenje koristeći min() i max() funkcije:

najmanji = min(niz)
najveći = max(niz)

print("Najmanji element niza:", najmanji)
print("Najveći element niza:", najveći)