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

    def siirrykerrokseen(self, kohdekerrokseen):
        while self.kerros != kohdekerrokseen:
            if self.kerros < kohdekerrokseen:
                self.kerros_ylos()
            if self.kerros > kohdekerrokseen:
                self.kerros_alas()
            elif kohdekerrokseen < self.alinkerros or kohdekerrokseen > self.ylinkerros:
                print(f'Hississä ei ole kerrosta {kohdekerrokseen}')
        return

h = Hissi(0,10)

print(f'Olet kerroksessa: {h.kerros}')
h.siirrykerrokseen(5)
print(f'Olet kerroksessa: {h.kerros}')
h.siirrykerrokseen(11)
print(f'Olet kerroksessa: {h.kerros}')