new_price = 0

product = "Lap xbox one"

laptops = ("I7", "I5", "I3", "A12", "A10", "A8")
tvs = ("CURVA", "SMART", "42\"", "40\"", "49\"", "45\"", "65\"", "60\"", "4K")
consolas = ("CONSOLA", "XBOX ONE", "PS4")
hogar = ("COLCHON", "SPLIT", "LAVADORA", "CAMA", "REFRIGERADOR", "ESTUFA")
hds = ("2TB", "3TB", "4TB")
celulares = ("XIAOMI", "ANDROID", "IPHONE", "APPLE", "SMARTPHONE")
chucherias = ("PLANCHA", "MICROONDAS", "PIZZAR", "MOCHILA", "PANTALON", "ZAPATO",
              "VESTIR", "TRAJE", "RELOJ", "TENIS", "BOXER")
personal = ("PERFUME", "DESO", "DESODORANTE", "ACNE", "ASEPXIA")
banned = ("FUNDA", "SOPORTE", "ADAPTADOR", "JUEGO", "CORREA", "WATCH", "MICA", "PROTECTOR", "ESTUCHE",
          "XBOX 360", "NO BREAK", "CABLE", "CONTROL")

filtrar = None

if any(keyword in product.upper() for keyword in banned):
    filtrar = False
else:
    filtrar = True

if (filtrar == True) and (new_price is not 0):
    #Buscamos
    if any(keyword in product.upper() for keyword in laptops):
        Status = 1
        if new_price <= 5000:
            Status = 0.1
        print Status
    elif any(keyword in product.upper() for keyword in tvs):
        Status = 2
        if new_price <= 4000:
            Status = 0.2
        print Status
    elif any(keyword in product.upper() for keyword in consolas):
        Status = 3
        if new_price <= 4000:
            Status = 0.3
        print Status
    elif any(keyword in product.upper() for keyword in hogar):
        Status = 4
        if new_price <= 1000:
            Status = 0.4
        print Status
    elif any(keyword in product.upper() for keyword in hds):
        Status = 5
        if new_price <= 1000:
            Status = 0.5
        print Status
    elif any(keyword in product.upper() for keyword in celulares):
        Status = 6
        if new_price <= 1000:
            Status = 0.6
        print Status
    elif any(keyword in product.upper() for keyword in chucherias):
        Status = 7
        if new_price <= 100:
            Status = 0.7
        print Status
    elif any(keyword in product.upper() for keyword in personal):
        Status = 8
        if new_price <= 25:
            Status = 0.8
        print Status
else:
    print("Banned words")


