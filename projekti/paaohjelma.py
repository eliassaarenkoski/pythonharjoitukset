from luokat import Hahmo
from luokat import Areena
from luokat import Ase
from luokat import Panssari
# areena oliot
areena1 = Areena("Capua","orja taistelija",100,50)
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
    pelaaja = Hahmo(pelaaja,100,150)
    print (f"Hahmon nimi on {pelaaja.nimi} ja elämäpisteitä on {pelaaja.hp}. Sinulla on {pelaaja.raha} verran kolikoita.")
    inventaario.append(ase4)
    return pelaaja
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
                    pelaaja.raha -= panssari1.hinta
                    print(f"Kolikoita jäi:{pelaaja.raha}. Rautapanssari listätty inventaarioon.")
                else:
                    print("\nSinulla ei ole tarpeeksi rahaa!\n")
            elif osto == "2":
                if pelaaja.raha >= panssari2.hinta:
                    inventaario.append(panssari2)
                    pelaaja.raha -= panssari2.hinta
                    print(f"Kolikoita jäi:{pelaaja.raha}. Kypärä listätty inventaarioon.")
                else:
                    print("\nSinulla ei ole tarpeeksi rahaa!\n")
            elif osto == "3":
                if pelaaja.raha >= panssari3.hinta:
                    inventaario.append(panssari3)
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
                    print(f"Kolikoita jäi:{pelaaja.raha}. Miekka listätty inventaarioon.")
                else:
                    print("\nSinulla ei ole tarpeeksi rahaa!\n")
            elif osto == "2":
                if pelaaja.raha >= ase2.hinta:
                    inventaario.append(ase2)
                    pelaaja.raha -= ase2.hinta
                    print(f"Kolikoita jäi:{pelaaja.raha}. Keihas listätty inventaarioon.")
                else:
                    print("\nSinulla ei ole tarpeeksi rahaa!\n")
            elif osto == "3":
                if pelaaja.raha >= ase3.hinta:
                    inventaario.append(ase3)
                    pelaaja.raha -= ase3.hinta
                    print(f"Kolikoita jäi:{pelaaja.raha}. Kolmikärki listätty inventaarioon.")
                else:
                    print("\nSinulla ei ole tarpeeksi rahaa!\n")
            elif osto == "4":
                if pelaaja.raha >= ase4.hinta:
                    inventaario.append(ase4)
                    pelaaja.raha -= ase4.hinta
                    print(f"Kolikoita jäi:{pelaaja.raha}. Tikari listätty inventaarioon.")
                else:
                    print("\nSinulla ei ole tarpeeksi rahaa!\n")
    else:
        return
def paavalikko():
    print("--Tervetuloa Päävalikkoon--")
    print("--Valitse vaihtoehto numeron mukaan")
    print("1. Tulosta ohjeet")
    print("2. Aloita uusi peli")
    print("3. Jatka peliä")
    print("4. Poistu")
    ehto = input("Valitse päävalikon toiminto (anna toiminnon nro) : ")
    if ehto == "1":
        print("peliä pelataan valitsemaalla eri toimintoja numero painikkeilla. Lue huolillisesti sillä voit myös kuluttaa rahaa tai hävitä.")
    elif ehto == "2":
        uusi_kayttäja()
    elif ehto == "3":
        print("tässä voisi ladata vanhan tallennuksen")
    else:
        print("kiitos sinulle pelaaja :D")
pelaaja = uusi_kayttäja()
kaupan_tulostus()

def areena_yksi():
    pass
def areena_kaksi():
    pass
def areena_kolme():
    pass
print(f"{inventaario[0].nimi}")
