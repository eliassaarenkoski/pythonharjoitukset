pituus = float(input("kuinka pitkä olet? :"))
ikä = int(input("kuika vanha olet?: "))

if pituus < 100:
    print ("et pääse laitteisiin")
elif 100 <= pituus <= 140:
    print ("saat mennä lasten laitteisiin.")
elif pituus <195:
    print ("et saa mennä kirnuun")
else:
    print (" saat mennä kaikkiin laitteisiin")