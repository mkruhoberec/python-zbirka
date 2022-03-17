#Omogućite proizvoljan unos brojeva. Zatim unesite te proizvoljne brojeve i ispitajte koliko ih
#ima parnih, a koliko neparnih.

broj_brojeva = int(input("Unesi broj brojeva: "))
sum_parnih = 0
sum_neparnih = 0

for i in range(broj_brojeva):
    broj = int(input("Unesi neki broj: "))
    if broj % 2 == 0:
        sum_parnih += 1
    elif broj % 2 == 1:
        sum_neparnih += 1

print("Zbroj parnih je:", sum_parnih, "\nZbroj neparnih je:",sum_neparnih)