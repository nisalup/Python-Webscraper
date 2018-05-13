from lxml import html
import requests
from Utilities import Utilities
from Website import Website

class WilliamHill:

    def scrapeWilliamHill(self):
        print('Scraping From WilliamHill started.')
        scrape_results = {}

        category_xpaths = "//a[normalize-space()='Football']"
        competition_xpaths = "//a[normalize-space()='World Cup 2018']"
        outrights_xpaths = "//a[contains(translate(., 'OUTRIGHT', 'outright'), 'outright')]"

        try:
            page = requests.get('http://sports.williamhill.com/bet/en-gb/betting/e/12085242/World+Cup+2018+-+Outright.html')
            tree = html.fromstring(page.content)
            odds = tree.xpath("//table[@class='tableData']//tbody//td[@scope='col']//div[@class='eventprice']/text()")
            countries = tree.xpath("//table[@class='tableData']//tbody//td[@scope='col']//div[@class='eventselection']/text()")
            scrape_results = Utilities.processResultData(odds, countries, Website.WILLIAMHILL)


        except Exception as ex:
            print('Exception at WilliamHill.py')
            print('Unchecked Error Occured')
            print(ex)

        print('Scrape results from Williamhill:')
        print(scrape_results)
        print('Scraping From Williamhill ended.')

        return scrape_results