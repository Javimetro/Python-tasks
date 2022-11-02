import random
class Auto:


    def __init__(self, rekisteritunnus,huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettumatka = 0

    def kiihdyta(self, nopeudenmuutos):
        self.nopeus += nopeudenmuutos
        huippunopeus = self.huippunopeus
        if self.nopeus >= huippunopeus:
            self.nopeus = huippunopeus
        elif self.nopeus <= 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.kuljettumatka += self.nopeus * tunnit

    def tulosta(self):
        print(f'\nREKISTERITUNNUS: {self.rekisteritunnus}\nHUIPPUNOPEUS: {self.huippunopeus} Km/h\nTÄMÄN HETKINEN NOPEUS: {self.nopeus} Km/h\nKULJETTU MATKA: {self.kuljettumatka} Km')


class Sahkoauto(Auto):

    def __init__(self, rekisteritunnus, huippunopeus, akku):
        self.akku = f'{akku}kWh'
        super().__init__(rekisteritunnus, huippunopeus)

    def tulosta(self):
        super().tulosta()
        print(f'AKKU: {self.akku}\nTYYPPI: {__class__.__name__}')

class Polttomoottoriauto(Auto):

    def __init__(self,rekisteritunnus, huippunopeus, tankki):
        self.tankki = f'{tankki} l'
        super().__init__(rekisteritunnus, huippunopeus)

    def tulosta(self):
        super().tulosta()
        print(f'TANKKI: {self.tankki}\nTYYPPI: {__class__.__name__}')

list = []
auto1 = Sahkoauto('ABC-15', 180, 52.5)
auto2 = Polttomoottoriauto('ACD-123', 180, 100)

list.append(auto1)
list.append(auto2)


for auto in list:
    auto.kiihdyta(100)
    auto.kulje(3)
    auto.tulosta()
