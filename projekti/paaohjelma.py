from luokat import Hahmo
from luokat import Areena
from luokat import Ase
from luokat import Panssari

import random
# areena oliot
areena1 = Areena("Capua","orja taistelija",90,40)
areena2 = Areena("Pompeji","Gladiaattori soturi",200, 50)
areena3 = Areena("Rooma","Mestariliigan soturi",500, 100)
# ase oliot
ase1 = Ase("miekka",50,50)
ase2 = Ase("keihas",80,70)
ase3 = Ase("kolmikarki",100,90)
ase4 = Ase("tikari",10,30)
# panssari oliot
panssari1 = Panssari("rautapanssari",100, 200)
panssari2 = Panssari("Kypärä",100, 50)
panssari3 = Panssari("Kilpi",100,100)
# listat mihin tulee läpäistyjen areenoiden alkiot ja inventaario lista kaupasta ostetuille tavaroille
lapaisyt = []
inventaario = []
# alla funtioita joita käytetään pelissä. Yksi on uuden hahmon luominen aloitus ominaisuuksilla. Toinen on toimiva kauppa missä voi ostaa tavaroita rahalla.
def uusi_kayttäja():

    pelaaja = input("Luo käyttäjän nimi : ")
    pelaaja = Hahmo(pelaaja,100, 0, 50)
    print (f"Hahmon nimi on {pelaaja.nimi} ja elämäpisteitä on {pelaaja.hp}. Sinulla on {pelaaja.raha} verran kolikoita.")
    inventaario.append(ase4)
    return pelaaja
#alla on kauppa funktio ja siinä voi ostaa rahalla tavaroita, jotka lisäävät joko elämäpisteitä tai vahinkoa. 
def kaupan_tulostus():
    print(f"---Tevetuloa markettiin---")
    print(f"---Marketista voit ostaa panssareita ja aseita")
    ehto = 0
    osto = 0
    while ehto != "3":
        ehto = input("Haluatko ostaa panssarin paina painiketta : 1 :\nHaluatko ostaa aseen paina painiketta : 2 :\nLopeta peli panamalla 3.\n")
        if ehto == "1":
            print("--- PANSSARIT ---")
            print(f"1. {panssari1.nimi} maksaa {panssari1.hinta} kolikko ja antaa {panssari1.hp} elämäpistettä.")
            print(f"2. {panssari2.nimi} maksaa {panssari2.hinta} kolikko ja antaa {panssari2.hp} elämäpistettä.")
            print(f"3. {panssari3.nimi} maksaa {panssari3.hinta} kolikko ja antaa {panssari3.hp} elämäpistettä.")
            print(f"\n Sinulla on tällä hetkellä kolikoita {pelaaja.raha} määrä")
            osto = input("Osta ase (syötä aseen nro) muussa tapauksessa paina enter")
            if osto == "1":
                if pelaaja.raha >= panssari1.hinta:
                    inventaario.append(panssari1)
                    pelaaja.max_hp += panssari1.hp
                    pelaaja.hp = pelaaja.max_hp
                    pelaaja.raha -= panssari1.hinta
                    print(f"Kolikoita jäi:{pelaaja.raha}. Rautapanssari listätty inventaarioon.")
                else:
                    print("\nSinulla ei ole tarpeeksi rahaa!\n")
            elif osto == "2":
                if pelaaja.raha >= panssari2.hinta:
                    inventaario.append(panssari2)
                    pelaaja.max_hp += panssari2.hp
                    pelaaja.hp = pelaaja.max_hp
                    pelaaja.raha -= panssari2.hinta
                    print(f"Kolikoita jäi:{pelaaja.raha}. Kypärä listätty inventaarioon.")
                else:
                    print("\nSinulla ei ole tarpeeksi rahaa!\n")
            elif osto == "3":
                if pelaaja.raha >= panssari3.hinta:
                    inventaario.append(panssari3)
                    pelaaja.max_hp += panssari3.hp
                    pelaaja.hp = pelaaja.max_hp
                    pelaaja.raha -= panssari3.hinta
                    print(f"Kolikoita jäi:{pelaaja.raha}. Kilpi listätty inventaarioon.")
                else:
                    print("\nSinulla ei ole tarpeeksi rahaa!\n") 

        elif ehto == "2":
            print("--- ASEET ---")
            print(f"1. {ase1.nimi} maksaa {ase1.hinta} kolikko ja tekee {ase1.vahinko} vahinkoa.")
            print(f"2. {ase2.nimi} maksaa {ase2.hinta} kolikko ja tekee {ase2.vahinko} vahinkoa.")
            print(f"3. {ase3.nimi} maksaa {ase3.hinta} kolikko ja tekee {ase3.vahinko} vahinkoa.")
            print(f"4. {ase4.nimi} maksaa {ase4.hinta} kolikko ja tekee {ase4.vahinko} vahinkoa.")
            print(f"\n Sinulla on tällä hetkellä kolikoita {pelaaja.raha} määrä")
            osto = input("Osta ase (syötä aseen nro) muussa tapauksessa paina enter")
            if osto == "1":
                if pelaaja.raha >= ase1.hinta:
                    inventaario.append(ase1)
                    pelaaja.raha -= ase1.hinta
                    pelaaja.vahinko += ase1.vahinko
                    print(f"Kolikoita jäi:{pelaaja.raha}. Miekka listätty inventaarioon.")
                else:
                    print("\nSinulla ei ole tarpeeksi rahaa!\n")
            elif osto == "2":
                if pelaaja.raha >= ase2.hinta:
                    inventaario.append(ase2)
                    pelaaja.raha -= ase2.hinta
                    pelaaja.vahinko += ase2.vahinko
                    print(f"Kolikoita jäi:{pelaaja.raha}. Keihas listätty inventaarioon.")
                else:
                    print("\nSinulla ei ole tarpeeksi rahaa!\n")
            elif osto == "3":
                if pelaaja.raha >= ase3.hinta:
                    inventaario.append(ase3)
                    pelaaja.raha -= ase3.hinta
                    pelaaja.vahinko += ase3.vahinko
                    print(f"Kolikoita jäi:{pelaaja.raha}. Kolmikärki listätty inventaarioon.")
                else:
                    print("\nSinulla ei ole tarpeeksi rahaa!\n")
            elif osto == "4":
                if pelaaja.raha >= ase4.hinta:
                    inventaario.append(ase4)
                    pelaaja.raha -= ase4.hinta
                    pelaaja.vahinko += ase4.vahinko
                    print(f"Kolikoita jäi:{pelaaja.raha}. Tikari listätty inventaarioon.")
                else:
                    print("\nSinulla ei ole tarpeeksi rahaa!\n")
    else:
        return
#päävalikotulostus funtkio. Antaa käyttäjän syötteestä ehdon.
def paavalikko():
    ehto=0
    while ehto != "4":
        print("--Tervetuloa Päävalikkoon--")
        print("--Valitse vaihtoehto numeron mukaan")
        print("1. Tulosta ohjeet")
        print("2. Aloita uusi peli")
        print("3. Jatka peliä")
        print("4. Poistu")
        ehto = input("Valitse päävalikon toiminto (anna toiminnon nro) : ")
        return ehto
# areena yksi funtkio. jossa taistelen painamalla enter painiketta. jokaisen painikkeen jälkeen tulostuu tilastot pisteistä. Peli jatkuu niin kauan kuin toisella ei ole enää elämäpisteitä  
def areena_yksi():
    print(f"---Tervetuloa ensimmäiseen areenaan!!! sinun tilastot ovat : {pelaaja.hp} elämäpistettä ja {pelaaja.vahinko} vahinkoa")
    print(f"Areena {areena1.paikka}. Vihollinen on {areena1.vihollinen}")
    input("Paina jotain kun olet valmis")
    vihollisen_hp = areena1.hp + random.randint(8, 13)
    vihollisen_vahinko = areena1.vahinko + random.randint(10, 10)
    pelaaja.hp = pelaaja.max_hp

    while pelaaja.hp > 0 and vihollisen_hp > 0:
        print(f"\nTaistelijan elämäpisteet: {pelaaja.hp}")
        print(f"Orjataistelijan elämäpisteet: {vihollisen_hp}")
        input("Paina Enter hyökätäksesi")
        vihollisen_hp -= pelaaja.vahinko
        if vihollisen_hp <= 0:
            break
        pelaaja.hp -= vihollisen_vahinko
    if vihollisen_hp <= 0:
        print("Voitit areenan!")
        pelaaja.raha += 100
    elif pelaaja.hp <= 0:
        print("Hävisit areenan!")
    input("Paina Enter palataksesi valikkoon...")
def areena_kaksi():
    print(f"---Tervetuloa toiseen areenaan!!! sinun tilastot ovat : {pelaaja.hp} elämäpistettä ja {pelaaja.vahinko} vahinkoa")
    print(f"Areena {areena2.paikka}. Vihollinen on {areena2.vihollinen}")
    input("Paina jotain kun olet valmis")
    vihollisen_hp = areena2.hp + random.randint(20, 25)
    vihollisen_vahinko = areena2.vahinko + random.randint(20, 25)
    pelaaja.hp = pelaaja.max_hp
    while pelaaja.hp > 0 and vihollisen_hp > 0:
        print(f"\nTaistelijan elämäpisteet: {pelaaja.hp}")
        print(f"Gladiaattorisoturin elämäpisteet: {vihollisen_hp}")
        input("Paina Enter hyökätäksesi")
        vihollisen_hp -= pelaaja.vahinko
        if vihollisen_hp <= 0:
            break
        pelaaja.hp -= vihollisen_vahinko
    if vihollisen_hp <= 0:
        print("Voitit areenan!")
        pelaaja.raha += 200
    elif pelaaja.hp <= 0:
        print("Hävisit areenan!")
    input("Paina Enter palataksesi valikkoon...")
def areena_kolme():
    print(f"---Tervetuloa viimeiseen areenaan!!! sinun tilastot ovat : {pelaaja.hp} elämäpistettä ja {pelaaja.vahinko} vahinkoa")
    print(f"Areena {areena3.paikka}. Vihollinen on {areena3.vihollinen}")
    input("Paina jotain kun olet valmis")
    vihollisen_hp = areena3.hp + random.randint(30, 35)
    vihollisen_vahinko = areena3.vahinko + random.randint(30, 30)
    pelaaja.hp = pelaaja.max_hp
    while pelaaja.hp > 0 and vihollisen_hp > 0:
        print(f"\nTaistelijan elämäpisteet: {pelaaja.hp}")
        print(f"Mestariliigan soturin elämäpisteet: {vihollisen_hp}")
        input("Paina Enter hyökätäksesi")
        vihollisen_hp -= pelaaja.vahinko
        if vihollisen_hp <= 0:
            break
        pelaaja.hp -= vihollisen_vahinko
    if vihollisen_hp <= 0:
        print("Voitit viimeisen areenan!")
        pelaaja.raha += 500
    elif pelaaja.hp <= 0:
        print("Hävisit areenan!")
    input("Paina Enter palataksesi valikkoon...")

import json
def tallenna_peli(pelaaja, lapaisyt, inventaario):
    tiedot = {"nimi": pelaaja.nimi,
        "hp": pelaaja.hp,
        "max_hp": pelaaja.max_hp,
        "raha": pelaaja.raha,
        "vahinko": pelaaja.vahinko,
        "lapaisyt": lapaisyt,
        "inventaario": [esine.nimi for esine in inventaario]}
    with open("tallennus.json", "w", encoding="utf-8") as tiedosto:
        json.dump(tiedot, tiedosto, indent=4, ensure_ascii=False)

def lataa_peli():
    with open("tallennus.json", "r", encoding="utf-8") as tiedosto:
        tiedot = json.load(tiedosto)
        pelaaja = Hahmo(tiedot["nimi"], 
                        tiedot["hp"], 
                        tiedot["raha"], 
                        tiedot["vahinko"]) 
        pelaaja.max_hp = tiedot["max_hp"] 
        return pelaaja

# pääohjelma

print("Tervetuloa pelaamaan! Joudumme valitettavasti tarkistamaan ikäsi jotta päähäsi ei satu.")
ika = int(input("Anna ikäsi: "))
if ika < 12:
    print("Et ole tarpeeksi vanha tälle pelille")
else:
    ehto = paavalikko()
    while ehto != "4":
        if ehto == "1":
            with open("readme.md", "r", encoding="utf-8") as tiedosto:
                ohjeet = tiedosto.read()

            print(f"{ohjeet}")
            input("\nPaina Enter palataksesi päävalikkoon...")
        elif ehto == "2":
            pelaaja = uusi_kayttäja()
            print("tervetuloa peliin!. Seuraavaksi voit läpäistä areenoita, käydä kaupassa ja katsoa hahmosi tilastoja. Onnea matkaan soturi!")
            print("Mitä haluaisit tehdä:\n1.Ensimmäinen areena(nro 1) : '\n2.Toinen Areena (nro2) :\n3.Viimeinen Areena (nro 3):\n4.Kauppa (nro 4) :\n5.Päävalikko (nro 5) : ")
            valinta = ""
            while valinta != "5":
                print("\nMitä haluaisit tehdä:")
                print("1. Ensimmäinen areena")
                print("2. Toinen areena")
                print("3. Viimeinen areena")
                print("4. Kauppa")
                print("5. Päävalikko")
                print("6. Tallenna")
                print("7. Katso tilasto")
                valinta = input("Anna valinta (nro): ")
                if valinta == "1":
                    areena_yksi()
                elif valinta == "2":
                    areena_kaksi()
                elif valinta == "3":
                    areena_kolme()
                elif valinta == "4":
                    kaupan_tulostus()
                elif valinta == "5":
                    print("Palataan päävalikkoon.")
                elif valinta =="6":
                    tallenna_peli(pelaaja, lapaisyt, inventaario)
                elif valinta == "7":
                    print(f"pelaajalla on:\n{pelaaja.hp} elämää\n{pelaaja.raha} kolikkoa\n{pelaaja.vahinko} vahinkoa")
                else:
                    print("Virheellinen valinta.")
        elif ehto == "3":
            pelaaja = lataa_peli()
            valinta = ""
            while valinta != "5":
                print("\nMitä haluaisit tehdä:")
                print("1. Ensimmäinen areena")
                print("2. Toinen areena")
                print("3. Viimeinen areena")
                print("4. Kauppa")
                print("5. Päävalikko")
                print("6. Tallenna")
                print("7. Katso tilasto")
                valinta = input("Anna valinta (nro): ")
                if valinta == "1":
                    areena_yksi()
                elif valinta == "2":
                    areena_kaksi()
                elif valinta == "3":
                    areena_kolme()
                elif valinta == "4":
                    kaupan_tulostus()
                elif valinta == "5":
                    print("Palataan päävalikkoon.")
                elif valinta =="6":
                    tallenna_peli(pelaaja, lapaisyt, inventaario)
                elif valinta == "7":
                    print(f"pelaajalla on:\n{pelaaja.hp} elämää\n{pelaaja.raha} kolikkoa\n{pelaaja.vahinko} vahinkoa")
                else:
                    print("Virheellinen valinta.")
            print(f"Tervetuloa takaisin {pelaaja.nimi}!")
        ehto = paavalikko()