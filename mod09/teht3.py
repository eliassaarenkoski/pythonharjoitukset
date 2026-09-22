# Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän. 
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt. 
# Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h. 
# Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 2000
  
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


auto1 = Auto("ABC-123", 142 )
print(f"Rekisteri on {auto1.rekisteritunnus} ja huippunopeus on {auto1.huippunopeus} km/h")
print (f"Uuden auton alkuarvot ovat. Kuljettu matka on {auto1.kuljettu_matka} ja tämänhetken nopeus on {auto1.tämänhetkinen_nopeus}")

auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)
auto1.kiihdyta(-200)
auto1.kiihdyta(60)
print(f"auto kulkee nyt {auto1.tämänhetkinen_nopeus}")
kulje1 = float(input("anna jokin tuntiluku: "))
auto1.kulje(kulje1)
print (f"Auto kulkee {auto1.kuljettu_matka} kilometriä nopeudella {auto1.tämänhetkinen_nopeus}")