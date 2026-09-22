pituus = float(input("kerro saamasi kuhan pituus: "))
isokoko = 37 - pituus

if pituus < 37:
    print (f"kuha on alipituinen. Laske se takaisin. {isokoko} cm puuttuu")
else:
    print("nauti kuhasta")