#Napisati program koji simulira bacanje novčića n puta te ispisati koliko puta se
#pojavljuje pismo i glava

from random import randint #randint koristimo za simuliranje bacanja novčića

broj_bacanja = int(input("Unesite broj bacanja: "))
pismo = 0 #Broj dobivenih pisama
glava = 0 #Broj dobivenih glava

for i in range(broj_bacanja):
    bacanje = randint(0,1) #Bacamo novčić
    if bacanje == 0:
        pismo += 1
    elif bacanje == 1:
        glava += 1

vjerojatnost_pismo = (pismo / broj_bacanja) * 100
vjerojatnost_glava = (glava / broj_bacanja) * 100

print("Vjerojatnost za pismo iznosi", vjerojatnost_pismo, "%")
print("Vjerojatnost za glavu iznosi", vjerojatnost_glava, "%")