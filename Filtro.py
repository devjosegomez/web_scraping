
def Get_Status_Category(Status, categoria, new_price, product):
    Status = None
    
    #Categorias
    laptops = (" I7 ", " I5 ", " I3 ", "AMD ", " A12 ", " A8 ", " A10 ", " A6 ")
    i7 = (" I7 ", " GTX")
    intel =("INTEL ", " inte ")
    tvs = ("CURVA ", " SMART", " 42\"", " 40\"", " 49\"", " 45\"", " 65\"", " 60\"", " 4K")
    consolas = ("CONSOLA", "XBOX ", "PS4 ")
    hogar = ("COLCHON", "SPLIT", "LAVADORA", "CAMA ", "REFRIGERADOR", "ESTUFA")
    hds = ("2TB", "3TB", "4TB", "8TB")
    celulares = ("XIAOMI ", " ANDROID", "IPHONE ", "APPLE ", "SMARTPHONE")
    chucherias = ("PLANCHA", "MICROONDAS", "PIZZAR", "MOCHILA", "PANTALON", "ZAPATO",
                  "VESTIR", "TRAJE", "RELOJ", "TENIS", "BACKPACK", "VINO ")
    personal = ("PERFUME", "DESOD", "DESODORANTE", "ACNE", "ASEPXIA", "CEREAL", "PACK ", "PAQUETE")
    banned = ("FUNDA", "SOPORTE", "ADAPTADOR", "JUEGO", "CORREA", "WATCH", "MICA", "PROTECTOR", "ESTUCHE",
              "XBOX 360", "NO BREAK", "CABLE", "CONTROL", "BRACERA", "REGULADOR", "PASS", "SUSCRIPCION",
              "CODIGO", "2DS", "S4 -", "ACTIVISION", "DISNEY", "CHATPAD", "ONE -", "SINTONIZADORA", "CARGADOR",
              "ARNES", "CHUPON", "POWERBANK", "PILA", "BATERIA", "LUZ", " STICKER ", "COOLING", "MOTHER", "MADRE",
              "VGO", "CALCOMONIA", "CUBIERTA", "PALMREST", "VJGO", "CURVAS", "CREMA", "MICROFIBRA", "CURVATION", "(XBO")

    filtrar = None
    categoria = ""

    if any(keyword in product.upper() for keyword in banned):
        filtrar = False
    else:
        filtrar = True

    if (filtrar == True) and (new_price is not 0):
        #Buscamos
        if any(keyword in product.upper() for keyword in laptops):
            Status = 1
            if new_price <= 7000:
                Status = 0.1
            print Status
            categoria = "Laptops"
        elif any(keyword in product.upper() for keyword in i7):
            Status = 1.1
            if new_price <= 10000:
                Status = 0.11
            print Status
            categoria = "i7"
        elif any(keyword in product.upper() for keyword in intel):
            Status = 1.2
            if new_price <= 4000:
                Status = 0.12
            print Status
            categoria = "Lap BARATA"
        elif any(keyword in product.upper() for keyword in tvs):
            Status = 2
            if new_price <= 5000:
                Status = 0.2
            categoria = "TVs"
            print Status
        elif any(keyword in product.upper() for keyword in consolas):
            Status = 3
            if new_price <= 5000:
                Status = 0.3
            categoria = "Consolas"
            print Status
        elif any(keyword in product.upper() for keyword in hogar):
            Status = 4
            if new_price <= 1000:
                Status = 0.4
            categoria = "Hogar"
            print Status
        elif any(keyword in product.upper() for keyword in hds):
            Status = 5
            if new_price <= 1000:
                Status = 0.5
            categoria = "HDs"
            print Status
        elif any(keyword in product.upper() for keyword in celulares):
            Status = 6
            if new_price <= 1000:
                Status = 0.6
            categoria = "Celulares"
            print Status
        elif any(keyword in product.upper() for keyword in chucherias):
            Status = 7
            if new_price <= 100:
                Status = 0.7
            categoria = "Chucherias"
            print Status
        elif any(keyword in product.upper() for keyword in personal):
            Status = 8
            if new_price <= 25:
                Status = 0.8
            categoria = "Personal"
            print Status

    #Return values of the status & category
    return (Status, categoria, new_price, product)
        
