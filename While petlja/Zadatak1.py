#Napisati program koji će korisniku dati mogućnost pogađanja lozinke. Mogućnost pogađanja
#lozinke izvršavati će se toliko puta dok korisnik ne pogodi lozinku. Kada korisnik pogodi
#lozinku, ispisati „upisali ste tocnu lozinku“ u suprotnom javiti vijest o pogrešno upisanoj
#lozinci i ponoviti unos.

password = ""

while password != "lozinka123":
    password = input("Unesite lozinku: ")
    if password == "lozinka123":
        print("Upisali ste točnu lozinku.")
    else:
        print("Upisali ste pogrešnu lozinku, pokušajte ponovno")