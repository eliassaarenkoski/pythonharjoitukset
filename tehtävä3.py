sukupuoli = input("mikä on suokupuolesi. Ilmoita mies tai nainen:")   
arvo = float(input(" ilmoita hemoglobiiniarvo g/l "))
    
if sukupuoli == "mies" and arvo <135 :
    print("alahainen hemoglobiini")
elif sukupuoli == "mies" and 135 <= arvo <= 195 :
    print("normaali hemoglobiini")
else : 
    sukupuoli == "mies" and arvo >195 
    print ("korkea hemoglobiini")

if sukupuoli == "nainen" and arvo <117 :
    print("alahainen hemoglobiini")
elif sukupuoli == "nainen" and 117 <= arvo <= 175  :
    print("normaali hemoglobiini")
else : 
    sukupuoli == "nainen" and arvo >175  
    print ("korkea hemoglobiini")
