#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. 
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.
syote = input("Anna luku: ")
if syote != "":
    pienin = float(syote)
    suurin = float(syote)
    while True:
        syote = input("Anna luku: ")
        if syote == "":
            break
        luku = float(syote)
        if luku < pienin:
            pienin = luku
        if luku > suurin:
            suurin = luku
    print("Pienin luku:", pienin)
    print("Suurin luku:", suurin)