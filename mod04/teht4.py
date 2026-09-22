karkausvuosi = int(input("anna karkausvuosi: "))
if karkausvuosi % 400 == 0 :
    print ("vuosi on karkausvuosi")
elif karkausvuosi % 4 == 0 and (karkausvuosi % 100 !=0) :
    print ("vuosi on karkausvuosi")
else:
    print ("vuosi ei ole karkausvuosi") 