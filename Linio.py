# -*- coding: utf-8 -*-
import json
import re
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.item import Item

class LinioSpider(scrapy.Spider):
    name = 'Linio'
    custom_settings = {
        'REDIRECT_ENABLED': False,
        'USER_AGENT': "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"
        }
    allowed_domains = ['linio.com.mx']
    filtro = 'is_international=0&sortBy=price_asc&page=%s'
    #Celulares
    categoria = 'https://www.linio.com.mx/c/celulares-y-tablets/celulares-y-smartphones?'
    quotes_base_url = categoria+filtro
    start_urls = [quotes_base_url % 1]

    def parse(self, response):
        self.log('---Extraction data ---')
        print (response.url)
        all_products = response.xpath('//div[@class="catalogue-product row"]')[0]

        for all_products in response.xpath('//div[@class="catalogue-product row"]'):
                try:
                        new_price = float(all_products.css('.price-secondary::text').extract_first().replace('$','').replace(',',''))
                except Exception:
                        new_price = 0
                try:
                        old_price = float(all_products.css('.original-price::text').extract_first().replace('$','').replace(',',''))
                except Exception:
                        old_price = 0

                try:
                        descuento = ((new_price / old_price) * 100.) -100 
                except Exception:
                        descuento = 0

                try:
                        url_product = all_products.css('div.catalogue-product > a::attr(href)').extract_first()
                        url_product = response.urljoin(url_product)
                except Exception:
                        url_product = all_products.css('div.catalogue-product > a::attr(href)').extract_first()

                try:
                        Status = None
                        product = all_products.css('span::text').extract_first()
                        
                        #Categorias
                        laptops = (" I5 ", " I3 ", "AMD ", " A8 ", " A10 ", " A6 ")
                        i7 = (" I7 ", " GTX", "A12", "GTX1080", "GTX 1080")
                        intel =("INTEL ", " ite ")
                        tvs = ("CURVA ", " SMART ", " 42\"", " 40\"", " 49\"", " 45\"", " 65\"", " 60\"", " 4K")
                        consolas = ("CONSOLA", "XBOX ", "PS4 ", "PLAYSTATION 4", "WII", "SWITCH ")
                        hogar = ("COLCHON", "SPLIT", "LAVADORA", "CAMA ", "REFRIGERADOR", "ESTUFA")
                        hds = ("2TB", "3TB", "4TB", "8TB", "SSD")
                        celulares = ("XIAOMI ", " ANDROID ", "IPHONE ", "APPLE ", "SMARTPHONE ")
                        chucherias = ("PLANCHA", "MICROONDAS", "PIZZAR", "MOCHILA", "PANTALON", "ZAPATO",
                                      "VESTIR", "TRAJE", "RELOJ", "TENIS", "BACKPACK", "VINO ")
                        personal = ("PERFUME", "DESOD", "DESODORANTE", "ACNE", "ASEPXIA", "CEREAL", "PACK ", "PAQUETE", "AXE ", "BARBA ")
                        banned = ("FUNDA", "SOPORTE", "ADAPTADOR", "JUEGO", "CORREA", "WATCH", "MICA", "PROTECTOR", "ESTUCHE",
                                  "XBOX 360", "NO BREAK", "CABLE", "CONTROL", "BRACERA", "REGULADOR", "PASS", "SUSCRIPCION",
                                  "CODIGO", "2DS", "S4 -", "ACTIVISION", "DISNEY", "CHATPAD", "ONE -", "SINTONIZADORA", "CARGADOR",
				  "ARNES", "CHUPON", "POWERBANK", "PILA", "BATERIA", "LUZ", " STICKER ", "COOLING", "MOTHER", "MADRE",
                                  "VGO", "CALCOMONIA", "CUBIERTA", "PALMREST", "VJGO", "CURVAS", "CREMA", "MICROFIBRA", "CURVATION",
                                  "(XBO", "TABLET", " 32\"")

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
                                categoria = "Laptops < 7000"
                            elif any(keyword in product.upper() for keyword in i7):
                                Status = 1.1
                                if new_price <= 10000:
                                    Status = 0.11
                                print Status
                                categoria = "Gamer"
                            elif any(keyword in product.upper() for keyword in intel):
                                Status = 1.2
                                if new_price <= 4000:
                                    Status = 0.12
                                print Status
                                categoria = "Laptops < 4000"
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

                except Exception:
                        product = ''

                yield {
                        'url_product':  url_product,
                        'product_name': product,
                        'new_price': new_price,
                        'old_price': old_price,
                        'descuento': descuento,
                        'Status': Status,
                        'Categoria': categoria
                        }

        current_page = response.url[-10:]
        current_page = re.sub("[^0-9]", "", current_page)
        current_page = int(current_page) + 1
        next_page = self.quotes_base_url % current_page
        
        Stop_spider = response.xpath('//*[contains(text(),"sin resultados")]').extract_first()
        if Stop_spider:
            print('Ya termine XD')
            raise CloseSpider('bandwidth_exceeded')
        else:
            yield scrapy.Request(url=next_page, callback=self.parse)
