from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from Utilities import Utilities
from Website import Website

class Bet365:

    def scrapeBet365(self):
        print('Scraping From Bet365 started.')
        scrape_results = {}
        driver = Utilities.getWebDriverWithoutProfile()
        try:
            driver.get('https://mobile.bet365.com/#type=Coupon;key=1-172-1-26326924-2-4-0-0-1-0-0-4063-0-0-1-0-0-0-0-0-75-0-0;ip=0;lng=1;anim=1')
            WebDriverWait(driver, int(Utilities.getWebDriverDefaultWait())).until(EC.presence_of_element_located((By.CLASS_NAME, 'podEventRow')))
            odds = driver.find_elements_by_xpath("//*[contains(@class,'podEventRow')]//*[@class='odds']")
            countries = driver.find_elements_by_xpath("//*[contains(@class,'podEventRow')]//*[@class='opp']")
            scrape_results = Utilities.processResultData(odds, countries, Website.BET365)

        except NoSuchElementException as ex:
            print('Exception at Bet365.py')
            print('The element could not be located or the xpath has changed.')
            print('If this is not the case, try increasing the timeout to allow more time for the website to load.')
            print('Error Message:')
            print(ex)
        except TimeoutException as ex:
            print('Exception at Bet365.py')
            print('The connection has been lost. Proxy addresses change regularly, so try with a new address')
            print('Error Message:')
            print(ex)
        except Exception as ex:
            print('Exception at Bet365.py')
            print('Unchecked Error Occured')
            print(ex)

        print('Scrape results from Bet365:')
        print(scrape_results)
        print('Scraping from Bet365 ended.')
        driver.quit()
        return scrape_results