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

autot = []
for i in range(1, 11):
    huippunopeus = random.randint(100, 200)
    auto = Auto(f"ABC-{i}", huippunopeus)
    autot.append(auto)
    
while True:
    for auto in autot:
        nopeuden_muutos = random.randint(-15,15)
        auto.kiihdyta(nopeuden_muutos)
        print(f"{auto.nopeuden_muutos}")

    for auto in autot:
        auto.kulje(1)

    for auto in autot:
        if auto.kuljettu_matka >= 10000:
                kilpailu_loppui = True
                break
    else:
        kilpailu_loppui = False

    if kilpailu_loppui:
        break

print(f"{'Rekisteritunnus':<18}{'Huippunopeus':<15}{'Nopeus':<15}{'Kuljettu matka':<15}")

for auto in autot:
    print(f"{auto.rekisteritunnus:<18}"
          f"{auto.huippunopeus:<15}"
          f"{auto.tämänhetkinen_nopeus:<15}"
          f"{auto.kuljettu_matka:<15.1f}")