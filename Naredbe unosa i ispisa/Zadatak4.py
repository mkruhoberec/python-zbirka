#Unesite znak preko tipkovnice (slovo,brojku, specijalni znak)
#Ispišite ASCII kod tog znaka.

znak = input("Unesite znak: ")
asci_kod = ord(znak) #ord() funkcija vraća ASCCI kod znaka

print("Znak je:", znak, "\nASCII vrijednost je:", asci_kod) #\n unutar teksta postavlja novu liniju teksta
