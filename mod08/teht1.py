# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan 
# (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen. 
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.

vuodenajat = ("talvi","kevät","kevät","kevät","kesä","kesä","kesä","syksy","syksy","syksy","talvi","talvi")
kuukausi = int(input("anna kuukausi 1-12 : "))
while vuodenajat != "":
    print(vuodenajat[kuukausi -1 ])
    kuukausi = int(input("anna kuukausi 1-12 : "))