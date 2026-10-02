class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

auto1 = Auto("ABC-123", 142 )
print(f"Rekisteri on {auto1.rekisteritunnus} ja huippunopeus on {auto1.huippunopeus} km/h")
print (f"Uuden auton alkuarvot ovat. Kuljettu matka on {auto1.kuljettu_matka} ja tämänhetken nopeus on {auto1.tämänhetkinen_nopeus}")