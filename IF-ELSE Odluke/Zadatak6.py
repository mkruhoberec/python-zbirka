#Upišite neku riječ. Provjerite nalazi li se u toj riječi samoglasnik a
#Ako se nalazi, ispisati samoglasnik se nalazi u napisanoj riječi, u suprotnom nema samoglasnika

rijec = input("Unesite neku riječ: ")
 
if "a" in rijec or "A" in rijec:
    print("Samoglasnik a se nalazi u riječi", rijec)
else:
    print("Samoglasnik a se ne nalazi u riječi", rijec)