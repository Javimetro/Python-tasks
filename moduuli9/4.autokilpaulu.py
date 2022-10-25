import random

class Auto:

    maaliviiva = 10000

    def __init__(self, rekisteritunnus,numero):
        self.rekisteritunnus = rekisteritunnus
        self.numero = numero
        self.huippunopeus = random.randint(100,200)
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
        print(f'REKISTERITUNNUS: {self.rekisteritunnus}\nHUIPPUNOPEUS: {self.huippunopeus} Km/h\nTÄMÄN HETKINEN NOPEUS: {self.nopeus} Km/h\nKULJETTU MATKA: {self.kuljettumatka} Km')


list = []

for i in range(10):
    auto = Auto(f'ABC-{i+1}',i+1)
    list.append(auto)

for self in list:
    while self.kuljettumatka <= 10000:
        self.kulje(1)
        self.kiihdyta(random.randint(-10,15))
    print(f'\nNo: {self.numero}\nREKISTERITUNNUS: {self.rekisteritunnus}\nHUIPPUNOPEUS: {self.huippunopeus} Km/h\nTÄMÄN HETKINEN NOPEUS: {self.nopeus} Km/h\nKULJETTU MATKA: {self.kuljettumatka} Km')
