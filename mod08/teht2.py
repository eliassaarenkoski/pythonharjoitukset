# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon. 
# Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan, syötettiinkö nimi ensimmäistä kertaa. 
# Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen.

#tehdään while toistorakenteesta while != "" : eli nyt kysymykset jatkuu kunnes syötetään tyhjä
# nimi = input ("anna nimi") tämä säilötään myös toistorakenteeseen jotta kysymykset jatkuvat niin kauan kuin toistorakenneen while ei toteudu
# tehdään lista nimille vaikka nimet =[ ] ja tehdään nimet.append(nimi) jotain tallaista
# kun meillä on mielivaltainen järjestys käytetään listaa set joka menee sulkeiden {} sisään
# nimet = []

# nimi = input("Anna ensimmäinen nimi tai lopeta painamalla Enter: ")
# while nimi != "":
#    nimet.append(nimi)
#    nimi = input("Anna seuraava nimi tai lopeta painamalla Enter: ")

nimet = set()
nimi = input("Anna nimi tai lopeta painamalla Enter: ")
while nimi != "":
    if nimi in nimet:
        print("Nimi löytyy jo listasta! ")
    else:
        print("Uusi nimi")
        nimet.add(nimi)

    nimi = input("Anna nimi tai lopeta painamalla Enter: ")
for nimi in nimet:
    print(nimi)