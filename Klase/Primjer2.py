class Automobil:
    def __init__(self, model, color):
        self.model = model
        self.color = color
    
    def display(self):
        print("Automobil je", self.model, self.color)

    def paint(self, new_color):
        self.color = new_color

punto = Automobil("Fiat", "Plava")

punto.display()

punto.paint("Crvena")

punto.display()