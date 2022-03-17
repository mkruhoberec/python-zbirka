#Unesite 2 broja. Ako su oba broja jednaka izračunati površinu kvadrata
#U suprotnom izračunati površinu pravokutnika

a = int(input("Unesite prvi broj: "))
b = int(input("Unesite drugi broj: "))

if a == b:
    p = a * a
    print("Površina kvadrata iznosi:", p)
else:
    p = a * b
    print("Površina pravokutnika iznosi", b)