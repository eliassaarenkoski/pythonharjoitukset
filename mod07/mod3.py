# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän. 
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen. 
# Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
# Yksi gallona on 3,785 litraa.

# itselle muistiin, mikäli luku 3785 merkitään pilkulla tulee luvusta vissiin tuple joka teki itselle pahan mielen hetkeksi

def muunnos(gallons):
    return gallons * 3.785

while True:
    gallons = float(input("anna gallonmäärä: "))

    if gallons < 0:
        break

    litra = muunnos(gallons)
    print(f"muunnos galloonista litraksi on {litra:2.3f} litraa.")