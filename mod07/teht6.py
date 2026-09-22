# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina. 
# Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri. 
# Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle 
# (eli kummalla on alhaisempi yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

#1 def joku nimi (parametri float halkaisija, perametsi hinta float)
#2 yksineliömetri on = 1€ tehdään funktiolle lauseke, jolla saadaan laskettua neliömetrit kertaa eurot
# pintaala = math.pi * (halkaisija / 2) ** 2
# yksikköhinta = hinta / pitntaala * 10000

# input luodaan käyttäjän syötteestä halkaisija arvo ja hinta arvo
# jokin ratkaisi ehkä if pitaala euroa suurempi kuin vaihtoehto toinen print eka vaihtoehto
# else print toinen vaihteehto
import math

def yksikkohinta(halkaisija, hinta):
    pintaala = math.pi * (halkaisija / 2) ** 2
    yksikkohinta = hinta / pintaala * 10000
    return yksikkohinta

halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija (cm): "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta (€): "))
halkaisija2 = float(input("Anna toisen pizzan halkaisija (cm): "))
hinta2 = float(input("Anna toisen pizzan hinta (€): "))

hintaperpa1 = yksikkohinta(halkaisija1, hinta1)
hintaperpa2 = yksikkohinta(halkaisija2, hinta2)
if hintaperpa1 < hintaperpa2:

    print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
else:
    print("Toinen pizza antaa paremman vastineen rahalle.")