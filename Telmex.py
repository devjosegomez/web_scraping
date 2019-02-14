# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.item import Item

class TelmexSpider(scrapy.Spider):
    name = 'Telmex'
    allowed_domains = ['tienda.telmex.com']
    DOWNLOADER_MIDDLEWARES = {'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,}

    quotes_base_url = "https://tienda.telmex.com/shell/af/core/search/search.do?contentTypeId=&categoryId=&selectedChannels=&paginationKey=&itemsPerPage=&returnFields=ProdName%7CPrice%7CStock%7CPreviewImage%7CShortDescription%7CLongDescription%7CMrPartId%7CCaracteristica1%7CCaracteristica2%7CCaracteristica3%7CCaracteristica4%7CCaracteristica5%7CCaracteristica6%7CCaracteristica7%7CCaracteristica8%7CCaracteristica9%7CCaracteristica10%7CProdId%7COID"
    filtro = "&pageNumber=%s&pageCount=92&query=a&perfilID=" %1
    quotes_base_url = quotes_base_url+filtro
    start_urls = [quotes_base_url]
    

    def parse(self, response):
        self.log('---Extraction data ---')
        
        all_products = response.xpath('//div[@class="div_prod-espec"]')[0]

        for all_products in response.xpath('//div[@class="div_prod-espec"]'):
            
                try:
                        new_price = float(all_products.css('span.txt_precio_azul::text').extract_first().strip().replace('$','').replace(',',''))
                        
                except Exception:
                        new_price = float(all_products.css('span.txt_precio_azul::text').extract_first().strip().replace('$','').replace(',',''))

                try:
                        meses = float(all_products.css('div.div_desc-espec span.txt_desde_azul::text').extract_first().strip().replace('$','').replace(',','').replace('meses:',''))

                except Exception:
                        meses = float(all_products.css('div.div_desc-espec span.txt_desde_azul::text').extract_first().strip().replace('$','').replace(',','').replace('meses:',''))
                            
                try:
                        new_price = (new_price * meses)

                except Exception:
                        new_price = 0

                try:
                        url_product = all_products.css('div.div_desc-espec span.tit_descprod a::attr(href)').extract_first()
                        url_product = response.urljoin(url_product)
                except Exception:
                        url_product = all_products.css('div.div_desc-espec span.tit_descprod a::attr(href)').extract_first()

                try:
                        Status = None
                        product = all_products.css('div.div_desc-espec span.tit_descprod a::text').extract_first().strip()
                        
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
                        'old_price': 0,
                        'descuento': 0,
                        'Status': Status,
                        'Categoria': categoria
                        }
        #Get page number
        filtro = '&pageNumber='
        posNextPage = response.request.url.find(filtro)
        NumPage = (re.sub("[^0-9]", "", response.request.url[posNextPage+len(filtro):posNextPage+len(filtro)+5]))
        Next_page = (int(NumPage) + 1)
        #Make url
        temp_url = "https://tienda.telmex.com/shell/af/core/search/search.do?contentTypeId=&categoryId=&selectedChannels=&paginationKey=&itemsPerPage=&returnFields=ProdName%7CPrice%7CStock%7CPreviewImage%7CShortDescription%7CLongDescription%7CMrPartId%7CCaracteristica1%7CCaracteristica2%7CCaracteristica3%7CCaracteristica4%7CCaracteristica5%7CCaracteristica6%7CCaracteristica7%7CCaracteristica8%7CCaracteristica9%7CCaracteristica10%7CProdId%7COID"
        filtro = "&pageNumber=%s&pageCount=92&query=a&perfilID=" %Next_page
        next_page_url = temp_url+filtro
        
        
        try:
            print('###################### ' + NumPage + ' ######################')
            yield scrapy.Request(url=next_page_url, callback=self.parse)
            print('#####################################################')
            print('#####################################################')

        except Exception:
            raise CloseSpider('bandwidth_exceeded')          
