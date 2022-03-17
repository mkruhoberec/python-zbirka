#Izračunati aritmetičku sredinu sedam brojeva.
#NAPOMENA: U jednoj liniji koda napraviti unos vrijednosti 7 varijabli.

broj1, broj2, broj3, broj4, broj5, broj6, broj7 = input("Unesi broj: ").split() #ovaj zadatak sam jedino uspio riješiti koristeći split()
aritmeticka_sredina = (broj1 + broj2 + broj3 + broj4 + broj5 + broj6 + broj7) / 7

print("Aritmetička sredina je:", aritmeticka_sredina)