from lxml import html
import requests
from Utilities import Utilities
import re

class WilliamHill:

    def scrapeWilliamHill(self):
        print('Scraping From WilliamHill started.')
        regex = re.compile('[^a-zA-Z]')
        odds_decoded = []
        countries_decoded = []
        scrape_results = {}
        try:
            page = requests.get('http://sports.williamhill.com/bet/en-gb/betting/e/12085242/World+Cup+2018+-+Outright.html')
            tree = html.fromstring(page.content)
            odds = tree.xpath("//table[@class='tableData']//tbody//td[@scope='col']//div[@class='eventprice']/text()")
            countries = tree.xpath("//table[@class='tableData']//tbody//td[@scope='col']//div[@class='eventselection']/text()")

            for odd in odds:
                data = Utilities.removeEscapeData(odd)
                data = data.strip()
                odds_decoded.append(data)

            for country in countries:
                data = Utilities.removeEscapeData(country)
                data = data.strip()
                data = regex.sub('', data).lower()
                data = re.sub(r'\s+', '', data)
                countries_decoded.append(data)

        except Exception as ex:
            print('Exception at WilliamHill.py')
            print('Unchecked Error Occured')
            print(ex)

        if len(countries_decoded) == len(odds_decoded):
            i = 0
            for item in countries_decoded:
                scrape_results[item] = odds_decoded[i]
                i += 1

        print('Scrape results from Williamhill:')
        print(scrape_results)
        print('Scraping From Williamhill ended.')

        return scrape_results