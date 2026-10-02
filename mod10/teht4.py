import random
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0
  
    def kiihdyta (self, nopeuden_muutos):
        self.nopeuden_muutos = nopeuden_muutos
        self.tämänhetkinen_nopeus += nopeuden_muutos
        if self.tämänhetkinen_nopeus >= self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus
        elif self.tämänhetkinen_nopeus <= 0:
            self.tämänhetkinen_nopeus = 0

    def kulje (self, tuntimaara):
        self.tuntimaara = tuntimaara
        self.kuljettu_matka = self.kuljettu_matka + self.tämänhetkinen_nopeus * tuntimaara

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeuden_muutos = random.randint(-15, 15)
            auto.kiihdyta(nopeuden_muutos)

        for auto in self.autot:
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"\n{self.nimi}")
        print(f"{'Rekisteritunnus':<18}{'Huippunopeus':<15}{'Nopeus':<15}{'Kuljettu matka':<15}")

        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<18}{auto.huippunopeus:<15}{auto.tämänhetkinen_nopeus:<15}{auto.kuljettu_matka:<15.1f}")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False

autot = []
for i in range(1, 11):
    huippunopeus = random.randint(100, 200)
    auto = Auto(f"ABC-{i}", huippunopeus)
    autot.append(auto)

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)
tunnit = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunnit += 1
    if tunnit % 10 == 0:
        kilpailu.tulosta_tilanne()
kilpailu.tulosta_tilanne()