from lxml import html
import requests
from Utilities import Utilities

class WilliamHill:



    def scrapeWilliamHill(self):
        odds_decoded=[]
        countries_decoded=[]
        scrape_results = []

        try:
            page = requests.get('http://sports.williamhill.com/bet/en-gb/betting/e/12085242/World+Cup+2018+-+Outright.html')
            tree = html.fromstring(page.content)

            odds = tree.xpath("//table[@class='tableData']//tbody//td[@scope='col']//div[@class='eventprice']/text()")
            countries = tree.xpath(
                "//table[@class='tableData']//tbody//td[@scope='col']//div[@class='eventselection']/text()")

            for odd in odds:
                data = Utilities.removeEscapeData(odd)
                data = data.strip()
                odds_decoded.append(data)

            for country in countries:
                data = Utilities.removeEscapeData(country)
                data = data.strip()
                countries_decoded.append(data)
        except:
            print("Unchecked Error Occured")

        scrape_results.append(countries_decoded)
        scrape_results.append(odds_decoded)
        return scrape_results


