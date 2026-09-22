# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. tehty! 
# Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa. tehty!
# Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. tehty !
# Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen. tehty !
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa. tehty !
# (ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)

# Tehdään tyhjä lista lentokonekentille sanakirja listana josta ICAO koodi toimii avaimena lentokonekentän kentän nimen tulostukseen.
# tehdään päävalikko 1,2,ja 3.1 voi lisätä listaan uuden lentoaseman nimen ja ICAO koodin toimii lista.idd tai lista.addend
# 2 voidaan etsiä icao koodilla lentoasemia 
# for ICAO in lentokonekentät(listan nimi)
# print (icao)
# käytetään input toimintoa arvojen saamiseksi ja while toimintoa jatkuvan kysymyksien saamiseksi. While == "3": kun käyttäjä painaa 3 tulee while toteen ja päättyy
# Helsinki-Vantaa: HEL / EFHK
# Oulu: OUL / EFOU
# Tampere-Pirkkala: TMP / EFTP
# Turku: TKU / EFTU
# Vaasa: VAA / EFVA

lentokenttä = {}
def päävalikko():
    print("päävalikko\n1. Syötä lentokentän nimi ja ICAO koodi: \n2. Etsi ICAO koodilla lentokentän tiedot: \n3. Lopeta ohjelma")
päävalikko()
toiminto = input("valitse toiminto 1-3: ")
while toiminto != "3":
    if toiminto == "1":
        lentokenttä1= input ("anna lentokenttä : ")
        koodi = input ("anna ICAO koodi valitulle lentokentälle : ")
        lentokenttä[koodi] = lentokenttä1
        päävalikko()
        toiminto = input("valitse toiminto 1-3: ")   
    elif toiminto == "2":
        koodi1 = input("Etsi lentokenttä ICAO-koodilla: ")
        print(lentokenttä[koodi1])
        päävalikko()
        toiminto = input("Valitse toiminto 1-3: ")
    else:
        break