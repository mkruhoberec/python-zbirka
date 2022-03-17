class Dog:
    def __init__(self, ime, boja):
        self.ime = ime
        self.boja = boja

    def display(self):
        print("Podaci o psu:", self.ime, self.boja)

    def farba(self, nova_boja):
        self.boja = nova_boja


pesek1 = Dog("Đuro", "Plava")

pesek1.display()

pesek1.farba("Crvena")

pesek1.display()