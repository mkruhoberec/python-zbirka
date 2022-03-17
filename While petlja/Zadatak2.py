#Napraviti program koji će korisniku omogućiti pogađanje brojeva. Ako korisnik upiše bilo
#koji broj, izvršavati će se blok naredbi ispod while petlje. Ako odabere 0, dogodi se prekid
#programa. Prekid programa omogućiti sa naredbom break. Ako korisnik upiše točan broj,
#ispiše se poruka o pogođenom broju i program se dalje izvršava. Ako korisnik napiše prevelik
#ili premali broj od traženog, ispisati prigodnu poruku korisniku i dalje izvršavati program,
#sve dok korisnik sma ne odabere opciju 0.

print("Igra pogađanja brojeva.")
print("Za prekid igre unesite 0.")

odgovor = 15
run = True

while run:
    broj = int(input("Unesite broj: "))
    if broj == odgovor:
        print("Pogodili ste zadani broj!")
        run = False
    elif broj == 0:
        run = False
    elif broj > odgovor:
        print("Broj je veći od zadanog, pokušajte ponovno.")
    elif broj < odgovor:
        print("Broj je manji od zadanog, pokušajte ponovno.")