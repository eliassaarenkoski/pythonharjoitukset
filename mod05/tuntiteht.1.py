komento = input(" valtise + - * tai seis ")
while komento != "seis" :
    if komento == "+":
        komentoplus1 = float(input(f"anna luku: "))
        komentoplus2 = float(input(f"anna luku: "))
        komentoyhteensa = komentoplus1 + komentoplus2
        print(f" {komentoyhteensa}")
    if komento == "-":
        komentoplus1 = float(input(f"anna luku: "))
        komentoplus2 = float(input(f"anna luku: "))
        komentovahennus = komentoplus1 - komentoplus2
        print(f" {komentovahennus}")
    if komento == "*":
        komentoplus1 = float(input(f"anna luku: "))
        komentoplus2 = float(input(f"anna luku: "))
        komentokerroin = komentoplus1 * komentoplus2
        print(f" {komentokerroin}")

    komento = input(" valtise + - * tai seis ")   
#luo laskin
#laskin antaa käyttäjän tehdä laskutoimituksia kunnes hän päättää lopettaa
#laskun tulostaa käyttäjälle valikon, josta hän voi valita jonkin kolmesta laskutoimituksesta (plus, miinus, kertolasku) tai lopetuksen
#jos käyttäjä ei valitse lopetusta, laskun pyytää käyttäjältä kaksi numeroa, ja tulostaa laskutoimituksen tuloksen

#laskin sitten tulostaa valikon uudestaa , ja käyttäjä voi valita uuden laskutoimituksen