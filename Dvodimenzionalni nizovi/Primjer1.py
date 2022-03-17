
matrica = []

matrica.append([1, 2, 3])
matrica.append([4, 5, 6])
matrica.append([7, 8, 9])

print("Ispis cijele matrice: ")

for red in matrica:
    print(red)

for red in matrica:
    print("\n")
    for element in red:
        print(element, end="  ")

print("Zadnji element u zadnjem redu: ", matrica[2][2])