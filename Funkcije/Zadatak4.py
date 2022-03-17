def parnost(x):
    if x % 2 == 0:
        print("Broj", x, "je paran.")
    elif x % 2 == 1:
        print("Broj", x, "je neparan.")

def negativnost(x):
    if x < 0:
        print("Broj", x,  "je negativan.")
    elif x > 0:
        print("Broj", x, "je pozitivan.")
    elif x == 0:
        print("Broj je nula.")

broj = int(input("Unesite neki broj: "))

parnost(broj)
negativnost(broj)