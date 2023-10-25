class däggdjur:
    def __init__(self, Hjärt_kammare):
        self.Hjärt_kammare = Hjärt_kammare

    def BlidGravid(self):
        print("bara att vänta")


class landdjur:
    def __init__(self, max_hastighet):
        self.max_hastighet = max_hastighet

    def gå(self):
        print("walking on sunshine")


class äggdjur:
    def __init__(self, max_ägg):
        self.max_ägg = max_ägg

    def läggÄgg(self):
        print("ägg har framkallats")


class havsDjur:
    def __init__(self, MaxDjup):
        self.MaxDjup = MaxDjup

    def simma(self):
        print("blup blup")


class val(däggdjur, havsDjur):
    def __init__(self, Hjärt_kammare, MaxDjup):
        super().__init__(Hjärt_kammare)
        havsDjur.__init__(self, MaxDjup)

    def eko(self):
        print("bip bip")


valle = val(4, 50)
