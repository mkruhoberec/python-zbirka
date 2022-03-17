#Napišite program koji će unositi broj učenika te omogućiti unos visine učenika
#prema broju unesenih učenika.
#Program treba ispisati visinu najnižeg i najvišeg učenika

broj_ucenika = int(input("Unesi broj učenika: "))
broj_ponavljanja = broj_ucenika

najvisi = 0
najnizi = 0

for i in range(broj_ponavljanja):
    visina = float(input("Unesi visinu učenika: "))
    if i == 0: #Prvo ponavljanje
        najnizi = najvisi = visina
    if visina > najvisi:
        najvisi = visina
    elif visina < najnizi:
        najnizi = visina

print("Najniži:", najnizi)
print("Najviši", najvisi)