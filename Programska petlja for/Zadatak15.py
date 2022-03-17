#Napisati program za učitavanje temperature zraka u prethodnih 10 dana te ispisati
#srednju temperaturu iznad nule i srednju temperaturu ispod nule.

suma_iznad_nule = 0
broj_temperatura_iznad_nule = 0

suma_ispod_nule = 0
broj_temperatura_ispod_nule = 0

broj_ponavljanja = 10

for i in range(broj_ponavljanja):
    temperatura = int(input("Unesi temperaturu: "))
    if temperatura < 0:
        suma_ispod_nule += temperatura
        broj_temperatura_ispod_nule += 1
    elif temperatura >= 0:
        suma_iznad_nule += temperatura
        broj_temperatura_iznad_nule += 1

prosjek_iznad_nule = suma_iznad_nule / broj_temperatura_iznad_nule
prosjek_ispod_nule = suma_ispod_nule / broj_temperatura_ispod_nule

print("Srednja temperatura iznad nule", round(prosjek_iznad_nule, 2))
print("Srednja temperatura ispod nule", round(prosjek_ispod_nule, 2))