# Projekti 3. Päävalikon toiminnot ja “inventaario”
# Kehitä peliprojektia eteenpäin: Luo jokaiselle päävalikon toiminnolle (joita vähintään kolme) oma funktio, joka suoritetaan, kun käyttäjä valitsee kyseisen toiminnon.
# Yhden funktion pitää kysyä käyttäjältä asioita (esim. esine), jotka lisätään listamuuttujaan.
# Toisen funktion pitää tulostaa listan sisältö käyttäjälle.
# Muut toiminnot voi ideoida ja toteuttaa vapaasti.

import random
nimi = input("Arvoisa pelaaja! Luo käyttäjä: ")
ika = int(input("Mikä on ikäsi?: "))
lisays = []
def lasku1():
    luku1 = random.randint(2, 10)
    luku2 = random.randint(2, 10)
    vastaus = float(input(f"Laske lausekkeen arvo {luku1} * {luku2} = : "))
    if vastaus == luku1 * luku2:
        print("Vastaus on oikein!")
    else:
        print("Vastaus on väärin!")
        return
def lasku2():
    luku3 = random.randint(5, 15)
    luku4 = random.randint(3, 4)
    print("anna vastau kokonaislukuina")
    vastaus = float(input(f"Laske lausekkeen arvo {luku3} / {luku4} = : "))
    if vastaus == luku3 // luku4:
        print("Vastaus on oikein!")
    else:
        print("Vastaus on väärin!")
def lisaa_esine():
    esine = input("Minkä esineen haluat lisätä inventaarioon?: ")
    lisays.append(esine)
    print(f"{esine} lisättiin inventaarioon!")
def nayta_inventaario():
    print("INVENTAARIO")
    if len(lisays) == 0:
        print("Inventaario on tyhjä.")
    else:
        for esine in lisays:
            print(esine)
def lopeta_peli():
    print("Peli loppui!")

if ika < 12:
    print("Et ole tarpeeksi vanha tälle pelille")
else:
    komento = ""
    while komento != "5":
        print("\nTervetuloa päävalikkoon!")
        print("1. Aloita kertolaskut")
        print("2. Aloita jakolaskut")
        print("3. Lisää esine")
        print("4. Näytä esineet")
        print("5. Lopeta laskut")

        komento = input("Määritä päävalikon arvo luvuilla 1-5: ")
        if komento == "1":
            lasku1()
        elif komento == "2":
            lasku2()
        elif komento == "3":
            lisaa_esine()
        elif komento == "4":
            nayta_inventaario()
        elif komento == "5":
            lopeta_peli()
        else:
            print("Virheellinen valinta!")