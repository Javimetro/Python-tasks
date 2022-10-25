class Auto:

    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinennopeus = 0
        self.kuljettumatka = 0

    def tulosta(self):
        print(f'REKISTERITUNNUS: {self.rekisteritunnus}\nHUIPPUNOPEUS: {self.huippunopeus}\nTÄMÄN HETKINEN NOPEUS: {self.tamanhetkinennopeus}\nKULJETTU MATKA: {self.kuljettumatka}')

auto1 = Auto('ABC-123','142Km/h')
auto1.tulosta()