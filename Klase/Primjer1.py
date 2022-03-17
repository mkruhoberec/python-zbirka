class Posuda:
    def insertBiskvit(self, biskvit):
        self.biskvit = biskvit
    
    def getBiskvit(self):
        print(self.biskvit)

posuda = Posuda()

posuda.insertBiskvit("Domačica")

posuda.getBiskvit()