oikeatvastaukset = {
    1:"53",
    2:"140",
    3:"71",
    "tehtävä_4" : "3"
}

kayttajan_vastaukset = {}
pisteet = []

def tarkistus (tehtävä):
    if oikeatvastaukset[tehtävä] == kayttajan_vastaukset[tehtävä]:
        print("vastasit onneksi oikein! ")
        pisteet.append(kayttajan_vastaukset)
    else:
        print("vastasit päin veetä")

kayttajan_vastaukset[1] = input("\nTehtävä 1:\nmikä on 100 - 47 vastaus : ")
tarkistus(1)

kayttajan_vastaukset[2] = input("\nTehtävä 2:\nmikä on 70 * 2 : ")
tarkistus(2)

kayttajan_vastaukset[3] = input("\nTehtävä 3: \nmikä on 70 * 1 + 1: ")
tarkistus(3)

kayttajan_vastaukset["tehtävä_4"] = input("\n kerro 3: ")
tarkistus("tehtävä_4")
print(f"\nsinun vastaukset ovat  : {kayttajan_vastaukset}")
print(f"\noikeat vastaukset ovat : {oikeatvastaukset}")
print(f"\nsait pistettä {len(pisteet)}/4")