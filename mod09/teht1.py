# Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus ja kuljettu matka. 
# Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin. 
# Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi. 
# Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h). 
# Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

auto1 = Auto("ABC-123", 142 )
print(f"Rekisteri on {auto1.rekisteritunnus} ja huippunopeus on {auto1.huippunopeus} km/h")
print (f"Uuden auton alkuarvot ovat. Kuljettu matka on {auto1.kuljettu_matka} ja tämänhetken nopeus on {auto1.tämänhetkinen_nopeus}")