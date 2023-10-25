class Fordon:
    def kör(self):
        print("Nu kör vi!")


class Bil(Fordon):
    def tuta(self):
        print("Tuuut!!")


class SportBil(Bil):
    def kör(self):
        print("nu kör vi riktigt snabbt!!")


class cykel(Fordon):
    def plinga(self):
        print("pling pong!")


b = cykel()
b.kör()
a = SportBil()
a.kör()
