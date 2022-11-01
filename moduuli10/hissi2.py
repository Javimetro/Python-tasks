class Hissi:
    def __init__(self, alinkerros, ylinkerros):
        self.ylinkerros = ylinkerros
        self.alinkerros = alinkerros
        self.kerros = alinkerros

    def kerros_ylos(self):
        self.kerros += 1
        print(f'Hissi on kerroksessa{self.kerros}')
        return

    def kerros_alas(self):
        self.kerros -= 1
        print(f'Hissi on kerroksessa{self.kerros}')
        return

    def siirrykerrokseen(self, kohdekerros):
        while self.kerros != kohdekerros:
            if self.kerros < kohdekerros:
                self.kerros_ylos()
            if self.kerros > kohdekerros:
                self.kerros_alas()
            elif kohdekerros < self.alinkerros or kohdekerros > self.ylinkerros:
                print(f'Hississä ei ole kerrosta {kohdekerros}')
        return


class Talo:
    def __init__(self, ylinkerros, alinkerros, lkm):
        self.ylinkerros = ylinkerros
        self.alinkerros = alinkerros
        self.lkm = lkm
        self.hissi_lista = []
        for hissi in range(lkm):
            self.hissi = hissi + 1
            self.hissi_lista.append(Hissi(alinkerros,ylinkerros))
            print(f'Hissi {self.hissi} lisätty taloon')

    def aja_hissia(self, numero, kohdekerros):
        numero = self.hissi_lista[numero]
        if numero in self.hissi_lista:
            kohdekerros = h.siirrykerrokseen(kohdekerros)
            print(f' Ajetaan hisillä {self.hissi} kerrokseen {kohdekerros}')
        else:
            print('Valitsemasi hissi ei ole olemassa')


h = Hissi(0,10)
t1 = Talo(10,0,5)

t1.aja_hissia(1,9)

