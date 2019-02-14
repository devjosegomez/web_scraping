import pandas as pd
import csv
from StringIO import StringIO

def isInList(product):
    #Categorias
    allProducts = (" I7 ", " I5 ", " I3 ", " AMD ", " A12 ", " A10 ", " A8 ", " A6 ", " DELL ", " ACER ", " ALIENWARE ", " ASUS ", " RAM ", " HP ",
                   " A9 ", " GTX ", " LENOVO ", " TOSHIBA ", " NVIDIA ", " VAIO ", " COMPAQ ", "LAPTOP", "COMPUTADORA", "MONITOR",  #LAPTOPS
                   " CURVA ", " SMART ", " 32\"", " 42\"", " 40\"", " 49\"", " 45\"", " 65\"", " 60\"", " 4K ", "HISENSE", "PANTALLA", "TV", "TELEVI", #TVS
                   "CONSOLA", "XBOX ", "PS4 ", "PLAYSTATION 4", "WII", "SWITCH ", #CONSOLAS
                   "COLCHON", "SPLIT", "LAVADORA", "CAMA ", "REFRIGERADOR", "ESTUFA", "PLANCHA", "MICROONDAS", "PIZZAR", "PANTAL", "ZAPATO", #HOGAR
                   "2TB", "3TB", "4TB", "8TB", "SSD", "DISCO DURO", "MICRO SD", "1TB", " TB ", #HDS
                   "XIAOMI ", " ANDROID ", "IPHONE ", "APPLE ", "SMARTPHONE ", "CELULAR", "NOKIA", "MOTOROLA", "MOTO ", "HUAWEI", " SIM ", #CELULARES
                   "PERFUME", "DESOD", "DESODORANTE", "ACNE", "ASEPXIA", "CEREAL", "PACK ", "PAQUETE", "AXE ", "BARBA ", #PERSONAL)
                   "VESTIR", "TRAJE", "RELOJ", "TENIS", "BACKPACK", "VINO ", "SONIDO")
    
    banned = ("FUNDA", "SOPORTE", "ADAPTADOR", "JUEGO", "CORREA", "WATCH", "MICA", "PROTECTOR", "ESTUCHE",
              "XBOX 360", "NO BREAK", "CABLE", "CONTROL", "BRACERA", "REGULADOR", "PASS", "SUSCRIPCION",
              "CODIGO", "2DS", "S4 -", "ACTIVISION", "DISNEY", "CHATPAD", "ONE -", "SINTONIZADORA", "CARGADOR",
              "ARNES", "CHUPON", "POWERBANK", "PILA", "BATERIA", "LUZ", " STICKER ", "COOLING", "MOTHER", "MADRE",
              "VGO", "CALCOMONIA", "CUBIERTA", "PALMREST", "VJGO", "CURVAS", "CREMA", "MICROFIBRA", "CURVATION",
              "(XBO", "TABLET", "ACCESORIO", "PROTECTOR")

    if any(keyword in product.upper() for keyword in banned):
        filtrar = False
    else:
        filtrar = True

    if (filtrar == True):
        #Buscamos
        if any(keyword in product.upper() for keyword in allProducts):
            return True
            

myCSV = pd.read_csv("all.csv", usecols=[4,6], dtype={4: str, 6: str})

i=0

for cols in myCSV.itertuples():
    product = cols.product_name
    if isInList(product):   
        new_price = cols.new_price
        if new_price >0 and new_price <=1000:
            print product
            print new_price
            i+=1
            print i
    
        
    
##    if isInList(product): 
##        print product
##        print new_price

