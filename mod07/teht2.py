# Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän. 
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa. 
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

def heita_noppaa(silmaluku):
    return random.randint(1,silmaluku)

maks = int(input("Anna nopan maksimisilmäluku: "))
luku = heita_noppaa(maks)

while luku != maks:
    print(luku)
    luku = heita_noppaa(maks)

print(luku)