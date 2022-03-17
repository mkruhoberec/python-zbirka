#Upisati troznamenkasti broj. Ispisati broj koji 
#unosimo i njegov ekvivalent u binarnom sustavu

broj = int(input("Unesite troznamenkasti broj: ")) # int() funkcija pretvara argument u cijeli broj ako može

binarni_broj = bin(broj) #bin() funkcija pretvara broj u binarno broj

print("Broj je", broj, "Binarni broj je", binarni_broj)