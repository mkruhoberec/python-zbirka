class Pravokutnik:
    def inserStranice(self, a, b):
        self.a = a
        self.b = b
    
    def getPovrsina(self):
        self.povrsina = self.a * self.b
        print("Površina je:", self.povrsina)

    def getOpseg(self):
        self.opseg = 2*self.a + 2*self.b
        print("Opseg je:", self.opseg)

pravokutnik1 = Pravokutnik()

pravokutnik1.inserStranice(5, 4)

pravokutnik1.getOpseg()
pravokutnik1.getPovrsina()