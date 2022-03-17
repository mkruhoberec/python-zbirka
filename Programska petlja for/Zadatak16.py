#Napisati program koji će generirati tablicu množenja brojeva do 10
kolicnik1 = 0
kolicnik2 = 0

for red in range(10):
    print("\n") #Novi red
    kolicnik2 = 1
    kolicnik1 += 1
    for stupac in range(10):
        print("{0:5}".format(kolicnik1 * kolicnik2), end="")
        kolicnik2 += 1