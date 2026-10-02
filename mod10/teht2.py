class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def siirry_kerrokseen(self, numero):
        while self.kerros < numero:
            self.kerros_ylös()
        while self.kerros > numero:
            self.kerros_alas()

    def kerros_ylös(self):
        if self.kerros < self.ylin:
            self.kerros += 1
            print(f"Hissi on nyt kerroksessa {self.kerros}")

    def kerros_alas(self):
        if self.kerros > self.alin:
            self.kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.kerros}")

class Talo:
    def __init__(self, alin, ylin, hissien_maara):
        self.hissit = []
        for i in range(hissien_maara):
            hissi = Hissi(alin, ylin)
            self.hissit.append(hissi)

    def aja_hissia(self, hissin_numero, kohdekerros):
        hissi = self.hissit[hissin_numero]
        hissi.siirry_kerrokseen(kohdekerros)
talo = Talo(1, 10, 3)

talo.aja_hissia(0, 5)
talo.aja_hissia(1, 8)

talo.aja_hissia(0, 1)
talo.aja_hissia(1, 1)