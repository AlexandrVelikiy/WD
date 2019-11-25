from scrapy import Spider
import scrapy
from scrapy.selector import Selector
from allpointsfps.items import ApfpsItem
import re
import logging
from scrapy.utils.log import configure_logging
logger = logging.getLogger('Apfps')
logger.setLevel(logging.DEBUG)
logger = logging.getLogger('scrapy.spidermiddlewares.httperror')
configure_logging(install_root_handler=False)
logging.basicConfig(
    filename='log.txt',
    format='%(levelname)s: %(message)s',
    level=logging.INFO
)


CATEGORY =[
            "A-1 Compressors",
            "APW",
            "Accutemp",
            "Adamation",
            "Adcraft",
            "Alto-Shaam",
            "Amana",
            "American Cook Systems",
            "American Dish Service",
            "American Metalcraft",
            "American Range",
            "Anets",
            "Anthony",
            "Anvil America",
            "Arctic Air",
            "Ardco",
            "Atkins",
            "Atlas",
            "Attias",
            "Autofry",
            "AyrKing",
            "BKI (Barbeque King)",
            "Bakers Pride",
            "Bally",
            "Bar Maid",
            "Bastian Blessing",
            "Baxter",
            "Beckett",
            "Belleco",
            "Berkel",
            "Beverage Air",
            "Bevles",
            "Biro",
            "Bizerba",
            "Blakeslee",
            "Blendtec",
            "Blickman",
            "Blodgett",
            "Bloomfield",
            "Bobrick",
            "Bohn",
            "Bradley",
            "Brewmatic",
            "Brite Way",
            "Broaster",
            "Bunn",
            "C Cretors",
            "Cadco",
            "Caddy",
            "Cambro",
            "Canplas",
            "Captiveaire",
            "Carlisle Foodservice",
            "Carter Hoffmann",
            "Cecilware",
            "Champion",
            "Chicago Faucet",
            "Cleveland",
            "Cma Dishmachines",
            "Comark",
            "Comstock Castle",
            "Connerton",
            "Continental Refrigerator",
            "Cooper Thermometer",
            "Cornelius",
            "Crescor",
            "Cuno",
            "Curtis",
            "Custom Deli&#39;s",
            "Darling International",
            "Dean",
            "Delfield",
            "Dito Dean",
            "Dormont",
            "Doughpro",
            "Doyon",
            "Duke",
            "Dynamic Cooking Systems",
            "Dynamic Mixer",
            "Edlund",
            "Electro Freeze",
            "Electrolux",
            "Ember Glo",
            "Everpure",
            "FWE",
            "Farberware",
            "Fast",
            "Federal Industries",
            "Fetco",
            "Fisher Faucet",
            "Fisher Manufacturing",
            "Fogel",
            "Follett",
            "Franke",
            "Franklin Chef",
            "Frigidaire",
            "Frymaster",
            "Fusion",
            "Garland",
            "General Electric",
            "German Knife",
            "Giles",
            "Glass Maid",
            "Glastender",
            "Glenco",
            "Globe",
            "Grindmaster",
            "Groen",
            "Hamilton Beach",
            "Hatco",
            "Heatcraft",
            "Henny Penny",
            "Hickory",
            "Hobart",
            "Hollymatic",
            "Holman",
            "Hoshizaki",
            "Howard",
            "Hubbell",
            "Hunter",
            "Hussmann",
            "Ice-O-Matic",
            "Imperial",
            "In-Sink-Erator",
            "Insinger",
            "Intedge",
            "Intek",
            "Intermetro",
            "Jackson",
            "Jade Range",
            "Jet Spray",
            "Kairak",
            "Keating",
            "Kelvinator",
            "Kitchen Aid",
            "Knight",
            "Kold Draft",
            "Kolpak",
            "Lang",
            "Legion",
            "Lejo",
            "Lincoln",
            "Lockwood",
            "Lucks",
            "MKE",
            "Magikitch&#39;N",
            "Manitowoc",
            "Market Forge",
            "Marsal And Sons",
            "Marshall Air",
            "Master-Bilt",
            "McCall",
            "McCray",
            "Meiko",
            "Merco",
            "Merrychef",
            "Metal Masters",
            "Middleby Marshall",
            "Miroil",
            "Moffat",
            "Montague",
            "Nemco",
            "Newco",
            "Nieco",
            "Nor-Lake",
            "Norris",
            "Nu-Vu",
            "Panasonic",
            "Peerless",
            "Perfect Fry",
            "Perlick",
            "Piper Products",
            "Pitco",
            "Power Soak Systems",
            "Precision Metal",
            "Premco",
            "Prince Castle",
            "Quality Industries",
            "Quickserv Corp",
            "Ranco",
            "Randell",
            "Rankin Delux",
            "Rational",
            "Raytek",
            "Redco",
            "Remcor",
            "Reynolds Mixer",
            "Rheem",
            "Rinnai",
            "Robot Coupe",
            "Rocky Mountain Cookware",
            "Roundup - AJ Antunes",
            "Royal Range",
            "Rubbermaid",
            "Russell",
            "Salvajor",
            "Sammic",
            "San Jamar",
            "Saniserv",
            "Savory",
            "Schaefer",
            "Scotsman",
            "Seco",
            "Selecto Scientific",
            "Server Products",
            "Sharp Microwave",
            "Shaver Specialty",
            "Silver King",
            "Slice Chief",
            "Sloan",
            "Southbend",
            "Southern Pride",
            "Standard Keil",
            "Star Mfg",
            "Sterling Multi-Mixer",
            "Stero",
            "Stoelting",
            "Sunkist",
            "Super Systems",
            "T&amp;S Brass",
            "TEC",
            "Taylor Freezer",
            "Taylor Thermometer",
            "Thermo Kool",
            "Toastmaster - See Middleby Marshall",
            "Town Foodservice Equipment",
            "Traex",
            "Traulsen",
            "Tri-Star",
            "True",
            "Turbo Air",
            "Turbochef",
            "Ultrafryer",
            "Unger Enterprises Inc USA",
            "Univex",
            "Uniworld",
            "Victory",
            "Vita-Mix",
            "Vollrath/Idea-Medalie",
            "Vulcan Hart",
            "Waring/Qualheim",
            "Warrick",
            "Welbilt",
            "Wells",
            "West Bend",
            "Wilbur Curtis - See Curtis",
            "Winston Products",
            "Wittco",
            "Wood Stone",
            "Worcester Industrial Products",
            "World Hand Dryer",
            "Zurn"
            ]

class APFSpider(Spider):
    name = "apf"
    allowed_domains = ["allpointsfps.com"]

    def start_requests(self):
        base_url = "https://www.allpointsfps.com/search/?oem="
        urls = CATEGORY

        for url in urls:
            logger.info(f'Start pars {url}')
            yield scrapy.Request(url=base_url+url+"&pageSize=100", meta={
                'dont_redirect': True,
                'handle_httpstatus_list': [302]}, callback=self.parse)

    def parse(self, response):

        oem = response.xpath('.//div[@class="intro-section "]/ul/li/text()').get()
        oem = oem.strip()
        oem = oem[oem.find(':')+1:].strip()

        urls = Selector(response).xpath('.//div [@ class="title-section"]/a/@href').extract()

        for url in urls:
            yield scrapy.Request(url='https://www.allpointsfps.com' + url,
                                 cb_kwargs=dict(oem=oem),
                                 callback=self.parse_item)

        # тул листаем по страницам пока они есть
        try:
            url_next_page = response.xpath('.//a[i/@class="icon icon-caret-right "]/@href').get()
            logger.info(f'Pares {url_next_page}')
            # ести есть то нажимаем и собираем ссылки
            yield scrapy.Request(url='https://www.allpointsfps.com' + url_next_page,
                                 callback=self.parse)

        except:
            pass  # ищем кнопку дальше, если нет то все
            logger.info('End of page')

    def parse_item(self,response,oem):
        items = ApfpsItem()

        items['url'] = response.url
        items['name'] = response.xpath('.//h1 [@class="title"]/text()').get()

        items['oem'] = self.get_oem(items['name'],oem)

        items['vendor'] = response.xpath('.//h4 [@class="sku-label"]/span/text()').get()
        try:
            items['image'] = response.xpath('.//a[@id="zoom"]/@href').get()
        except:
            items['image'] = '-'

        items['price'] = response.xpath('.//span [@itemprop="price"]/text()').get()
        try:
            oem_list = response.xpath('.//ul [@class="list-unstyled oem-skus"]/li/text()').getall()
            crossreference = ''
            for s in oem_list:
                crossreference = crossreference + s.strip()  +','
            items['crossreference'] = items['oem'] +","+ crossreference[:len(crossreference)-1]
        except:
            items['crossreference'] = items['oem']

        d = response.xpath('.//div [@class="description"]/p/text()').getall()
        description = ''
        for s in d:
            description = description + s.strip()+' '
        items['description'] = description.strip()

        items['manufacturerName'] = oem
        logger.info(f'~Store item {oem} name {items["name"]}')

        return items

    def get_oem(self,name, oem):
        try:
            tmp = []
            pre_str = ''

            if name.find(oem) == 0:
                # нашли с начала строки, так и добавим в начало
                pre_str = oem
            list_s = name.split(' ')
            # проверям что у нас за строки
            for s in list_s:
                if re.match("^[A-Za-z0-9_-]*$", s):
                    # цифры и буквы
                    if re.match("^[A-Za]*$", s):
                        continue # пропускаем
                    tmp.append(s)
                elif s =='-':
                    tmp.append(s)

            if pre_str:
                tmp.insert(0,pre_str)

            # если первый и последний символ - то удаляем их
            if tmp:
                if tmp[0] == '-':
                     tmp.pop(0)
                if tmp[len(tmp)-1] == '-':
                    tmp.pop(len(tmp) - 1)


            oem = ' '.join(tmp)

            return oem
        except:
            pass