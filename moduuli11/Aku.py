class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f'Julkaisun nimi: {self.nimi}')

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'Päätoimittaja on: {self.paatoimittaja}')

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja,sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'Kirjoittaja: {self.kirjoittaja}, sivujenmäärä: {self.sivumaara}')

j1 = Lehti('Aku Ankka', 'Aki Hyyppä')
j2 = Kirja('Hytti n:o 6', 'Rosa Liskom', 200)
j1.tulosta_tiedot()
j2.tulosta_tiedot()