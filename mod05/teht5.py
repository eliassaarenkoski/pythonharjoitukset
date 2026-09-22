#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan. 
#Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen. 
#Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa. 
#Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty. (Oikea käyttäjätunnus on python ja salasana rules).

tunnus = input("Anna käyttäjätunnus: ")
salasana = input("Anna salasana: ")

yritykset = 0

while yritykset < 5:
    if tunnus == "python" and salasana == "rules":
        print("Tervetuloa")
        break

    yritykset += 1

    if yritykset == 5:
        print("Pääsy evätty")
        break

    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")