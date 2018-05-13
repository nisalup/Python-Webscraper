from Utilities import Utilities
from Website import Website
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class WilliamHill:

    def scrapeWilliamHill(self):
        print('Scraping From WilliamHill started.')
        scrape_results = {}


        category_xpaths = "//a[normalize-space()='Football']"
        competition_xpaths = "//a[normalize-space()='World Cup 2018']"
        outrights_xpaths = "//a[contains(translate(., 'OUTRIGHT', 'outright'), 'outright')]"

        try:
            driver = Utilities.getWebDriverJSDisabled()
            driver.get('http://sports.williamhill.com/bet/en-gb/betting/e/12085242/World+Cup+2018+-+Outright.html')
            WebDriverWait(driver, int(Utilities.getWebDriverDefaultWait())).until(EC.presence_of_element_located((By.CLASS_NAME, 'eventprice')))
            odds = driver.find_elements_by_xpath("//table[@class='tableData']//tbody//td[@scope='col']//div[@class='eventprice']")
            countries = driver.find_elements_by_xpath("//table[@class='tableData']//tbody//td[@scope='col']//div[@class='eventselection']")
            scrape_results = Utilities.processResultData(odds, countries, Website.WILLIAMHILL)


        except NoSuchElementException as ex:
            print('Exception at WilliamHill.py')
            print('The element could not be located or the xpath has changed.')
            print('If this is not the case, try increasing the timeout to allow more time for the website to load.')
            print('Error Message:')
            print(ex)
        except TimeoutException as ex:
            print('Exception at WilliamHill.py')
            print('The connection has been lost. Proxy addresses change regularly, so try with a new address')
            print('Error Message:')
            print(ex)
        except Exception as ex:
            print('Exception at WilliamHill.py')
            print('Unchecked Error Occured')
            print(ex)

        print('Scrape results from Williamhill:')
        print(scrape_results)
        print('Scraping From Williamhill ended.')
        driver.quit()
        return scrape_results