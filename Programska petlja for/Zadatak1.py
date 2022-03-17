#Ispišite ponavljanje rečenice „Unosimo policu broj“ deset puta.

broj_police = 1 #Početna vrijednost broja police
broj_ponavljanja = 10 #Broj ponavljanja

for i in range(broj_ponavljanja):
    print("Unosimo policu broj", broj_police)
    broj_police += 1 #U svakom koraku povećavamo broj police za 1