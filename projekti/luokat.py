class Hahmo:
    def __init__(self, nimi, hp, raha, vahinko):
        self.nimi = nimi
        self.hp = hp
        self.max_hp = hp
        self.raha = raha
        self.vahinko = vahinko
class Areena:
    def __init__(self, paikka, vihollinen,hp, vahinko):
        self.paikka = paikka
        self.vihollinen = vihollinen
        self.hp = hp
        self.vahinko = vahinko  
class Esine:
    def __init__(self, nimi, hinta):
        self.nimi = nimi
        self.hinta = hinta
class Ase(Esine):
    def __init__(self, nimi, hinta, vahinko):
        super().__init__(nimi,hinta)
        self.vahinko = vahinko      
class Panssari(Esine):
    def __init__(self,nimi,hinta, hp):
        super().__init__(nimi,hinta)
        self.hp = hp