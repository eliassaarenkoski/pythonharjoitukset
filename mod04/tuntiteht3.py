olympiavuosi = int(input("anna olympiavuosi: "))
if olympiavuosi % 4 == 0 and olympiavuosi != 2020:
    print (f"{olympiavuosi} on olympiaisvuosi")
elif olympiavuosi == 2020 :
    print ("poikkeuksellisesti ei ollut koronan vuoksi ja ne pidetiin 2021 sen sijasta")
elif olympiavuosi == 2021 :
    print ("oli poikkeuksellisesti olympialaisvuosi")
else: 
    print (f"{olympiavuosi} ei ollut olympiaisvuosi.")