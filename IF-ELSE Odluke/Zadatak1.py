#Unesi neki prirodan broj i provjeri je li taj broj djeljiv sa sedam

broj = int(input("Unesite broj: "))

if broj % 7 == 0:
    print("Broj", broj, "je djeljiv sa sedam.")
else:
    print("Broj", broj, "nije djeljiv sa sedam.")