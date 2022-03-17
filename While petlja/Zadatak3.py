#Program treba tražiti od korisnika unos broja u rasponu od 10-20. Ukoliko korisnik pogodi
#raspon; ispisati: cestitamo-unijeli ste broj u rasponu i ispisati broj kojeg je korisnik unio.
#Ako korisnik ne pogodi broj, ispisati: broj nije u rasponu od 10-20; Pokušajte ponovno.
#Petlja se izvršava tako dugo dok je uvjet na TRUE odnosno dok korisnik unosi brojeve veće
#od nula. Ako korisnik unese 0 odnosno FALSE, prekida se izvođenje programa.

run = True

while run:
    broj = int(input("Unesite broj u rasponu od 10 do 20: "))
    if broj >= 10 and broj <= 20:
        print("Čestitamo unijeli ste broj u rasponu,", broj)
    elif broj == 0:
        print("Izlazak iz programa.")
        run = False
    elif broj < 10 or broj > 20:
        print("Broj nije u rasponu od 10 do 20.")
        print("Pokušajte ponovno")