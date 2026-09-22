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
        
        
auto1 = Auto("ABC-123", 142 )
print(f"Rekisteri on {auto1.rekisteritunnus} ja huippunopeus on {auto1.huippunopeus} km/h")
print (f"Uuden auton alkuarvot ovat. Kuljettu matka on {auto1.kuljettu_matka} ja tämänhetken nopeus on {auto1.tämänhetkinen_nopeus}")

auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)
auto1.kiihdyta(-200)
print(f"auto kulkee nyt {auto1.tämänhetkinen_nopeus}")