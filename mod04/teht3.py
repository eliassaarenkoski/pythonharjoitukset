#Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l). Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

sukupuoli = input("kerro biologinen sukupuolesi: ")
arvo = float(input("anna hemoglobiini arvosi: "))

if sukupuoli == "mies" and arvo < 134:
    print(f"hemoglobiiniarvo on alhainen")
elif sukupuoli == "mies" and 134<= arvo <=195:
    print(f"hemoglobiiniarvo on normaali")
elif sukupuoli == "mies" and arvo > 195:
    print(f"hemoglobiiniarvo on korkea")

if sukupuoli == "nainen" and arvo < 117:
    print(f"hemoglobiiniarvo on alhainen")
elif sukupuoli == "nainen" and 117<= arvo <=175:
    print(f"hemoglobiiniarvo on normaali")
elif sukupuoli == "nainen" and arvo > 175:
    print(f"hemoglobiiniarvo on korkea")