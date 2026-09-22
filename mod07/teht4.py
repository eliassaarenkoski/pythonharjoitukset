# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. 
# Ohjelma palauttaa listassa olevien lukujen summan. 
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

def summa(lukulista):
    summa = 0
    for luku in lukulista:
        summa +=luku
    return summa
lukulista = [1, 2, 3, 4, 5, 6]
tulos = summa(lukulista)
print(tulos)