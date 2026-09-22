# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. 
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. 
# Käytä for-toistorakennetta.
import random
luku = int(input("anna arpakuutioiden lukumäärä : "))
noppaluku = random.randint(1,6)
summa = 0

for n in range(luku): 
    noppaluku = random.randint(1, 6) 
    summa += noppaluku

print(f"arpakuutioiden summa on : {summa}")