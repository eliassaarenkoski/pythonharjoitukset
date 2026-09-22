pituus = float(input("kuinka pitkä olet: "))

if pituus <100 : 
    print("et pääse laitteisiin")

elif 100 <= pituus <= 140:
    ika = int(input("kuinka vanha olet :"))
    if ika >=8 and pituus >=140:
        print("saat myös mennä tulirekeen")
    print ("saat mennä lasten laitteisiin.")
    
    
else:
    print("pääset kaikkiin laitteisiin")
    if pituus >= 195:
        print("pääset kaikkiin laitteisiin paitsi kirnuun")