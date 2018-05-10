from lxml import html
import requests
from Utilities import Utilities

class WilliamHill:



    def scrapeWilliamHill(self):
        odds_decoded=[]
        countries_decoded=[]

        page = requests.get('http://sports.williamhill.com/bet/en-gb/betting/e/12085242/World+Cup+2018+-+Outright.html')
        tree = html.fromstring(page.content)

        odds = tree.xpath("//table[@class='tableData']//tbody//td[@scope='col']//div[@class='eventprice']/text()")
        countries = tree.xpath("//table[@class='tableData']//tbody//td[@scope='col']//div[@class='eventselection']/text()")

        for odd in odds:
            data = Utilities.removeEscapeData(odd)
            odds_decoded.append(data)

        for country in countries:
            data = Utilities.removeEscapeData(country)
            countries_decoded.append(data)

        print(odds_decoded)
        print(countries_decoded)


