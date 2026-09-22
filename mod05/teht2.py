#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän. 
# Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm
tuuma = float(input("anna tuumamäärä: ")) 
while tuuma >= 0: 
    tuumacm = tuuma * 2.54 
    print(f"{tuumacm} cm") 
    tuuma = float(input("anna tuumamäärä: ")) 
print("ohjelma loppui")