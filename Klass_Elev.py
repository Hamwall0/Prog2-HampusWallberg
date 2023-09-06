class Elev:
    def __init__(self, namn, ålder, betyg):
        self.namn = namn
        self.ålder = ålder
        self.betyg = betyg
        if self.betyg == "godkänd":
            self.humör = "glad"

    def Presentera(self):
        print("Hej! jag heter", self.namn)


elev1 = Elev("Hampus", "18", "underkänd")
elev2 = Elev("Isak", "18", "godkänd")
elev1.Presentera()
