nimi = input("anna nimesi: ")
print (f"{nimi} oli suuri soturi ja {nimi} seuraa uljaasti soturin tietä. \nLeikkaatko kaljun terällä vai koneella?")
vastaus = input("kumman valitset? vastaa kone tai tera: ")

if vastaus == "kone":
    print(f" {nimi} on häpeksi soturin tielle.")
if vastaus == "tera":
    print(f" {nimi} tekee soturin tien ylpeksi valinnallaan")