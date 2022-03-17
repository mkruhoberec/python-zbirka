#Sljedeći program je konkretan prikaz primjene matrica u svrhu tabličnog skladištenja
#podataka. Sljedeća matrica skladišti podatke kao što su jmbg, ime, prezime. Ujedno ispisuje
#posljednji element matrice na indeksu [2][2]. 

datoteka = []
datoteka.append([344321, "Pero", "Perić"])
datoteka.append([563345, "Ivo", "Ivić"])
datoteka.append([123566, "Jozo", "Jozić"])

for slog in datoteka:
    print(slog)


print("Čisti ispis svih polja")
print("JMBAG, Ime, Prezime")
print("--------------------")
for slog in datoteka:
    print("\n")
    for polje in slog:
        print(polje, end=" ")