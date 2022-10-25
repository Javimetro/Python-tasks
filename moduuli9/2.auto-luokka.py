class Auto:

    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettumatka = 0

    def kiihdyta(self, nopeudenmuutos):
        self.nopeus += nopeudenmuutos
        huippunopeus = 142
        if self.nopeus >= huippunopeus:
            self.nopeus = 142
        elif self.nopeus <= 0:
            self.nopeus = 0

    def tulosta(self):
        print(f'REKISTERITUNNUS: {self.rekisteritunnus}\nHUIPPUNOPEUS: {self.huippunopeus} Km/h\nTÄMÄN HETKINEN NOPEUS: {self.nopeus} Km/h\nKULJETTU MATKA: {self.kuljettumatka} Km')

auto1 = Auto('ABC-123','142')
auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)
auto1.kiihdyta(-200)
auto1.tulosta()