import random
class Djur:
    def __init__(self,namn):
        self.namn = namn

class Fågel(Djur):
    def __init__(self,namn,vingspann):
        super().__init__(namn)
        self.vingspann = vingspann
class Fisk(Djur):
    def __init__(self, namn,maxdjup):
        super().__init__(namn)
        self.maxdjup = maxdjup
class Torsk (Fisk):
    def __init__(self, namn, maxdjup,hastighet):
        super().__init__(namn, maxdjup)
        self.hastighet = hastighet
class Haj(Fisk):
    def __init__(self, namn, maxdjup,antaltänder):
        super().__init__(namn, maxdjup)
        self.antaltänder = antaltänder
        
bert = Torsk("Bert",random.randint(50,100),random.randint(10,65))
harry = Haj("Harry",int(random.randint(10,65)),int(random.randint(500,1000)))

def Fånga(a,b):
    if a.hastighet < 30 and b.maxdjup >= a.hastighet:
        print("True")
    else:
        print("False")
Fånga(bert,harry)
#hej