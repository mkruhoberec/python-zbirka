#Upisati jednu riječ i umnožiti je 5 puta.

rijec = input("Unesi jednu riječ: ")
print(5 * rijec)
print(5 * (rijec + " ")) #Ako želimo razmak

#alternativno riješenje

umnozak_rijeci = rijec * 5
print(umnozak_rijeci)

#alternativno rješenje s razmakom
umnozak_rijeci = (rijec + " ") * 5
print(umnozak_rijeci)