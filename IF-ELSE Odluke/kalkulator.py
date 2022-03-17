izbor = input("Unesi željenu operaciju: ")

if "+" in izbor:
    print("Izabrano zbrajanje (+)")
    broj1 = float(input("Unesi prvi broj: "))
    broj2 = float(input("Unesi drugi broj: "))
    zbroj = broj1 + broj2 
    print("Zbroj je", zbroj)
elif "-" in izbor:
    print("Izabrano oduzimanje (-)")
    broj1 = float(input("Unesi prvi broj: "))
    broj2 = float(input("Unesi drugi broj: "))
    razlika = broj1 - broj2 
    print("Razlika je", razlika)
elif "*" in izbor:
    print("Izabrano množenje (*)")
    broj1 = float(input("Unesi prvi broj: "))
    broj2 = float(input("Unesi drugi broj: "))
    umnozak = broj1 * broj2 
    print("Umnozak je", umnozak)
elif "/" in izbor:
    print("Izabrano djeljenje (/)")
    broj1 = float(input("Unesi prvi broj: "))
    broj2 = float(input("Unesi drugi broj: "))
    kolicnik = broj1 / broj2 
    print("Količnik je", kolicnik)
else:
    print("Nije izabrana dobra operacija,\nMolim upisati: /,*,- ili +.")