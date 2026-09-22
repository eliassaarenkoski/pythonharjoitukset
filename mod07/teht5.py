# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. 
# Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut. 
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

#okei luodaan pää ohjelma jossa listassa on luvut 1-13
#tehdään funktio joka saa listan, mutta funktion tarkoitus on karsia parittomat luvut
#tulostetaan alkuperäinen listä ja tulostetaan funktiolla karsittu lista

def listamuuttuja(lista1):
    karsittu = []
    for x in lista1:
        if x % 2 == 0:
            karsittu.append(x)
    return karsittu
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print("Alkuperäinen lista:", lista1)
print("Karsittu lista:", listamuuttuja(lista1))